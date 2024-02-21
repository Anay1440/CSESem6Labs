#include <stdio.h>
#include <CL/cl.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// Max source size of the kernel string
#define MAX_SOURCE_SIZE (0x100000)
int main(void) {

    time_t start, end;
    start = clock();

    char str[100];
    int n;

    // Initialize the input string

    printf("Enter string ");
    scanf("%s", str);

    printf("Enter n ");
    scanf("%d", &n);

    int len = strlen(str);

    // Load the kernel source code into the array source_str 
    FILE *fp;
    char *source_str;
    size_t source_size;
    fp = fopen("Q1vectorCLKernel.cl", "r");
    if (!fp)
    {
        fprintf(stderr, "Failed to load kernel.\n");
        getchar();
        exit(1);
    }
    source_str = (char *)malloc(MAX_SOURCE_SIZE);
    source_size = fread(source_str, 1, MAX_SOURCE_SIZE, fp);

    fclose(fp);

    // Get platform and device information 
    cl_platform_id platform_id = NULL; 
    cl_device_id device_id= NULL; 
    cl_uint ret_num_devices;
    cl_uint ret_num_platforms;

    cl_int ret = clGetPlatformIDs(1, &platform_id, &ret_num_platforms);
    ret = clGetDeviceIDs(platform_id, CL_DEVICE_TYPE_GPU, 1, &device_id, &ret_num_devices);
    // Create an OpenCL context
    cl_context context = clCreateContext(NULL, 1, &device_id, NULL, NULL, &ret);

    // Create a command queue
    cl_command_queue command_queue = clCreateCommandQueue(context, device_id, CL_QUEUE_PROFILING_ENABLE, &ret);

    // Create memory buffers on the device
    cl_mem s_mem_obj = clCreateBuffer(context, CL_MEM_READ_ONLY, len * sizeof(char), NULL, &ret);
    cl_mem len_mem_obj = clCreateBuffer(context, CL_MEM_READ_ONLY, sizeof(int), NULL, &ret);
    cl_mem t_mem_obj = clCreateBuffer(context, CL_MEM_WRITE_ONLY, len * n * sizeof(char), NULL, &ret);

    // Copy the string to the memory buffer
    ret = clEnqueueWriteBuffer(command_queue, s_mem_obj, CL_TRUE, 0, len * sizeof(char), str, 0, NULL, NULL);
    ret = clEnqueueWriteBuffer(command_queue, len_mem_obj, CL_TRUE, 0, sizeof(int), &len, 0, NULL, NULL);

    // Create a program from the kernel source
    cl_program program = clCreateProgramWithSource(context, 1, (const char **)&source_str, (const size_t *)&source_size, &ret);

    // Build the program
    ret = clBuildProgram(program, 1, &device_id, NULL, NULL, NULL);

    // C1eate the OpenCL kernel object
    cl_kernel kernel = clCreateKernel(program, "vector_copy_str", &ret);

    // Set the arguments of the kernel
    ret = clSetKernelArg(kernel, 0, sizeof(cl_mem), (void *)&s_mem_obj);
    ret = clSetKernelArg(kernel, 1, sizeof(cl_mem), (void *)&len_mem_obj);
    ret = clSetKernelArg(kernel, 2, sizeof(cl_mem), (void *)&t_mem_obj);

    // Execute the OpenCL kernel on the array 
    size_t global_item_size = n; 
    size_t local_item_size = 1;

    // Execute the kernel on the device 
    cl_event event;
    ret = clEnqueueNDRangeKernel(command_queue, kernel, 1, NULL, &global_item_size, &local_item_size, 0, NULL, NULL);

    // Kernel exec must be finished before calculating time
    ret = clFinish(command_queue);

    cl_ulong time_start, time_end;
    double total_time;

    // Find the kernel execution start time

    clGetEventProfilingInfo(event, CL_PROFILING_COMMAND_START, sizeof(time_start), &time_start, NULL);

    // Find the kernel execution end time

    clGetEventProfilingInfo(event, CL_PROFILING_COMMAND_END, sizeof(time_end), &time_end, NULL);

    total_time = (double) (time_end - time_start);

    // Read the memory buffer

    char * str_res = (char *) malloc(sizeof(char) * len * n);
    
    ret = clEnqueueReadBuffer(command_queue, t_mem_obj, CL_TRUE, 0, len * n * sizeof(char), str_res, 0, NULL, NULL);

    // Display the result
    
    str_res[n * len] = '\0';

    printf("Resultant string: %s\n", str_res);

    // Clean up
    ret = clReleaseKernel(kernel);
    ret = clReleaseProgram(program);
    ret = clReleaseMemObject(s_mem_obj);
    ret = clReleaseMemObject(len_mem_obj);
    ret = clReleaseMemObject(t_mem_obj);
    ret = clReleaseCommandQueue(command_queue);
    ret = clReleaseContext(context);

    end = clock();

    printf("\nTime taken to execute the kernel = %0.3f ms\n", total_time / 1000000);
    printf("Time taken to execute the whole program = %0.3f ms\n", (end - start) / (double) CLOCKS_PER_SEC);
    free(str_res);
    return 0;
}