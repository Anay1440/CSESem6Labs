#include <stdio.h>
#include <CL/cl.h>
#include <stdlib.h>
#include <time.h>

// Max source size of the kernel string
#define MAX_SOURCE_SIZE (0x100000)
int main(void) {

    time_t start, end;
    start = clock();

    int n;

    // Initialize the input string

    printf("Enter number of elements ");
    scanf("%d", &n);

    int * arr = (int *) malloc(sizeof(int) * n);

    for (int i = 0; i < n; i++) {
        printf("Enter arr[%d] ", i);
        scanf("%d", &arr[i]);
    }

    // Load the kernel source code into the array source_str 
    FILE *fp;
    char *source_str;
    size_t source_size;
    fp = fopen("Q3vectorCLKernel.cl", "r");
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
    cl_mem a_mem_obj = clCreateBuffer(context, CL_MEM_READ_WRITE, n * sizeof(int), NULL, &ret);

    // Copy to the memory buffer
    ret = clEnqueueWriteBuffer(command_queue, a_mem_obj, CL_TRUE, 0, n * sizeof(int), arr, 0, NULL, NULL);

    // Create a program from the kernel source
    cl_program program = clCreateProgramWithSource(context, 1, (const char **)&source_str, (const size_t *)&source_size, &ret);

    // Build the program
    ret = clBuildProgram(program, 1, &device_id, NULL, NULL, NULL);

    // C1eate the OpenCL kernel object
    cl_kernel kernel_odd_step = clCreateKernel(program, "vector_brick_sort_odd_step", &ret);
    cl_kernel kernel_even_step = clCreateKernel(program, "vector_brick_sort_even_step", &ret);

    // Set the arguments of the kernel
    ret = clSetKernelArg(kernel_odd_step, 0, sizeof(cl_mem), (void *)&a_mem_obj);
    ret = clSetKernelArg(kernel_even_step, 0, sizeof(cl_mem), (void *)&a_mem_obj);

    // Execute the OpenCL kernel on the array 
    size_t global_item_size = n;
    size_t local_item_size = 2;

    // Execute the kernel on the device 
    cl_event event;
    for (int i = 0; i < n / 2; i++) {
        global_item_size = n - 2;
        ret = clEnqueueNDRangeKernel(command_queue, kernel_odd_step, 1, NULL, &global_item_size, &local_item_size, 0, NULL, NULL);
        global_item_size = n;
        ret = clEnqueueNDRangeKernel(command_queue, kernel_even_step, 1, NULL, &global_item_size, &local_item_size, 0, NULL, NULL);
    }

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

    int * res_arr = (int *) malloc(sizeof(int) * n);
    
    ret = clEnqueueReadBuffer(command_queue, a_mem_obj, CL_TRUE, 0, n * sizeof(int), res_arr, 0, NULL, NULL);

    // Display the result

    printf("Sorted array: ");

    for (int i = 0; i < n; i++)
        printf("%d ", res_arr[i]);

    printf("\n");
    
    // Clean up
    ret = clReleaseKernel(kernel_odd_step);
    ret = clReleaseKernel(kernel_even_step);
    ret = clReleaseProgram(program);
    ret = clReleaseMemObject(a_mem_obj);
    ret = clReleaseCommandQueue(command_queue);
    ret = clReleaseContext(context);

    end = clock();

    printf("\nTime taken to execute the kernel = %0.3f ms\n", total_time / 1000000);
    printf("Time taken to execute the whole program = %0.3f ms\n", (end - start) / (double) CLOCKS_PER_SEC);
    free(arr);
    free(res_arr);
    return 0;
}