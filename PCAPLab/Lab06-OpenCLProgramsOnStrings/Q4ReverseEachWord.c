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

    int n, index = 0;

    // Initialize the input string

    printf("Enter number of elements ");
    scanf("%d", &n);

    char * arr = (char *) malloc(sizeof(char) * 1000);
    char * recv_arr = (char *) malloc(sizeof(char) * 1000);
    int * lengths = (int *) malloc(sizeof(int) * n);

    for (int i = 0; i < n; i++) {
        char temp[30];
        printf("Enter string no. %d ", i);
        scanf("%s", temp);
        lengths[i] = strlen(temp);
        for (int j = 0; j < lengths[i]; j++)
            arr[index++] = temp[j];
    }

    // Load the kernel source code into the array source_str 
    FILE *fp;
    char *source_str;
    size_t source_size;
    fp = fopen("Q4vectorCLKernel.cl", "r");
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
    cl_mem a_mem_obj = clCreateBuffer(context, CL_MEM_READ_WRITE, sizeof(char) * 1000, NULL, &ret);
    cl_mem len_mem_obj = clCreateBuffer(context, CL_MEM_READ_ONLY, n * sizeof(int), NULL, &ret);

    // Copy to the memory buffer
    ret = clEnqueueWriteBuffer(command_queue, a_mem_obj, CL_TRUE, 0, sizeof(char) * 1000 , arr, 0, NULL, NULL);
    ret = clEnqueueWriteBuffer(command_queue, len_mem_obj, CL_TRUE, 0, n * sizeof(int), lengths, 0, NULL, NULL);

    // Create a program from the kernel source
    cl_program program = clCreateProgramWithSource(context, 1, (const char **)&source_str, (const size_t *)&source_size, &ret);

    // Build the program
    ret = clBuildProgram(program, 1, &device_id, NULL, NULL, NULL);

    // C1eate the OpenCL kernel object
    cl_kernel kernel = clCreateKernel(program, "vector_rev_each_word", &ret);

    // Set the arguments of the kernel
    ret = clSetKernelArg(kernel, 0, sizeof(cl_mem), (void *)&a_mem_obj);
    ret = clSetKernelArg(kernel, 1, sizeof(cl_mem), (void *)&len_mem_obj);

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

    // clGetEventProfilingInfo(event, CL_PROFILING_COMMAND_START, sizeof(time_start), &time_start, NULL);

    // Find the kernel execution end time

    // clGetEventProfilingInfo(event, CL_PROFILING_COMMAND_END, sizeof(time_end), &time_end, NULL);

    // total_time = (double) (time_end - time_start);

    // Read the memory buffer
    
    ret = clEnqueueReadBuffer(command_queue, a_mem_obj, CL_TRUE, 0, sizeof(char) * 1000, recv_arr, 0, NULL, NULL);

    // Display the result

    printf("Final sentence: ");

    index = 0;
    for (int i = 0; i < n; i++) {
        char temp[30];
        int j;
        for (j = 0; j < lengths[i]; j++)
            temp[j] = recv_arr[index++];
        temp[j + 1] = '\0';
        printf("%s ", temp);
    }

    printf("\n");
    
    // Clean up
    ret = clReleaseKernel(kernel);
    ret = clReleaseProgram(program);
    ret = clReleaseMemObject(a_mem_obj);
    ret = clReleaseCommandQueue(command_queue);
    ret = clReleaseContext(context);

    end = clock();

    printf("\nTime taken to execute the kernel = %0.3f ms\n", total_time / 1000000);
    printf("Time taken to execute the whole program = %0.3f ms\n", (end - start) / (double) CLOCKS_PER_SEC);
    free(arr);
    return 0;
}