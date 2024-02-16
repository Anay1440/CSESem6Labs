#include <stdio.h>
#include <CL/cl.h>
#include <stdlib.h>
// Max source size of the kernel string
#define MAX_SOURCE_SIZE (0x100000)
int main(void) {
    int i, n, lengthOfNumber = 4;
    printf("Enter how many elements: ");
    scanf("%d", &n);

    char * A = (char *) malloc(sizeof(char) * n * lengthOfNumber);
    char * str = (char *) malloc(sizeof(char) * (lengthOfNumber + 1));

    // Initialize the input vectors 
    for (i = 0; i < n; i++) {
        printf("Enter arr[%d] (4 digits) ", i);
        scanf("%s", str);
        for (int j = 0; j < lengthOfNumber; j++)
            A[i * lengthOfNumber + j] = str[j];
    }

    // Load the kernel source code into the array source_str 
    FILE *fp;
    char *source_str;
    size_t source_size;
    fp = fopen("Q2VectorCLKernel.cl", "r");
    if (!fp) {
        fprintf(stderr, "Failed to load kernel.\n");
        getchar();
        exit(1);
    }
    source_str = (char *)malloc(MAX_SOURCE_SIZE);
    source_size = fread(source_str, 1, MAX_SOURCE_SIZE, fp);

    fclose(fp);

    // Get platform and device information int i = get_global_id(0);
    cl_platform_id platform_id = NULL; 
    cl_device_id device_id= NULL; 
    cl_uint ret_num_devices;
    cl_uint ret_num_platforms;

    cl_int ret = clGetPlatformIDs(1, &platform_id, &ret_num_platforms);
    ret = clGetDeviceIDs(platform_id, CL_DEVICE_TYPE_GPU, 1, &device_id, &ret_num_devices);
    // Create an OpenCL context
    cl_context context = clCreateContext(NULL, 1, &device_id, NULL, NULL, &ret);

    // Create a command queue
    cl_command_queue command_queue = clCreateCommandQueue(context, device_id, NULL, &ret);

    // Create memory buffers on the device for each vector A, B
    cl_mem a_mem_obj = clCreateBuffer(context, CL_MEM_READ_ONLY, n * lengthOfNumber * sizeof(char), NULL, &ret);
    cl_mem b_mem_obj = clCreateBuffer(context, CL_MEM_WRITE_ONLY, n * lengthOfNumber * sizeof(char), NULL, &ret);

    ret = clEnqueueWriteBuffer(command_queue, a_mem_obj, CL_TRUE, 0, n * lengthOfNumber * sizeof(char), A, 0, NULL, NULL);

    // Create a program from the kernel source
    cl_program program = clCreateProgramWithSource(context, 1, (const char **)&source_str, (const size_t *)&source_size, &ret);

    // Build the program
    ret = clBuildProgram(program, 1, &device_id, NULL, NULL, NULL);

    // C1eate the OpenCL kernel object
    cl_kernel kernel = clCreateKernel(program, "vector_ones_complement", &ret);

    // Set the arguments of the kernel
    ret = clSetKernelArg(kernel, 0, sizeof(cl_mem), (void *)&a_mem_obj);
    ret = clSetKernelArg(kernel, 1, sizeof(cl_mem), (void *)&b_mem_obj);

    // Execute the OpenCL kernel on the array 
    size_t global_item_size = n; 
    size_t local_item_size = 1;

    // Execute the kernel on the device 
    cl_event event;
    ret = clEnqueueNDRangeKernel(command_queue, kernel, 1, NULL, &global_item_size, &local_item_size, 0, NULL, NULL);
    ret = clFinish(command_queue);

    // Read the memory buffer on the device to the local variable B 
    char * B = (char *) malloc(sizeof(char) * n * lengthOfNumber);

    ret = clEnqueueReadBuffer(command_queue, b_mem_obj, CL_TRUE, 0, n * lengthOfNumber * sizeof(char), B, 0, NULL, NULL);
    
    // Display the result to the screen 
    
    char * str1 = (char *) malloc(sizeof(char) * (lengthOfNumber + 1));
    char * str2 = (char *) malloc(sizeof(char) * (lengthOfNumber + 1));
    
    for (i = 0; i < n; i++) {
        for (int j = 0; j < lengthOfNumber; j++) {
            str1[j] = A[i * lengthOfNumber + j];
            str2[j] = B[i * lengthOfNumber + j];
        }
        str1[lengthOfNumber] = '\0';
        str2[lengthOfNumber] = '\0';
        printf("%s one's complement = %s\n", str1, str2);
    }

    // Clean up
    ret = clFlush(command_queue);
    ret = clReleaseKernel(kernel);
    ret = clReleaseProgram(program);
    ret = clReleaseMemObject(a_mem_obj);
    ret = clReleaseMemObject(b_mem_obj);
    ret = clReleaseCommandQueue(command_queue);
    ret = clReleaseContext(context);
    free(A);
    free(B);
    getchar();
    return 0;
}