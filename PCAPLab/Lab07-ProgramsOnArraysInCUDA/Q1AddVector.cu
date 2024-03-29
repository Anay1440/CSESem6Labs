#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>

__global__ void add(int *a, int *b, int *c) {
    int index = blockIdx.x * blockDim.x + threadIdx.x;
    c[index] = a[index] + b[index];
}

int main(void) {
    int n;

    printf("Enter n ");
    scanf("%d", &n);

    // Host copies of vectors a, b, c
    int * a = (int *) malloc(n * sizeof(int));
    int * b = (int *) malloc(n * sizeof(int));
    int * c = (int *) malloc(n * sizeof(int));

    // Setup input values
    for (int i = 0; i < n; i++) {
        printf("Enter a[%d] and b[%d] ", i, i);
        scanf("%d %d", &a[i], &b[i]);
    }

    int *d_a, *d_b, *d_c; // Device copies of vectors a, b, c
    int size = n * sizeof(int);

    // Allocate space for device copies of a, b, c

    cudaMalloc((void **)&d_a, size);
    cudaMalloc((void **)&d_b, size);
    cudaMalloc((void **)&d_c, size);

    // Copy inputs to device

    cudaMemcpy(d_a, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, b, size, cudaMemcpyHostToDevice);

    // Launch add() kernel on GPU

    // Part a
    add<<<1, n>>>(d_a, d_b, d_c);

    // Part b
    // add<<<n, 1>>>(d_a, d_b, d_c);

    // Copy result back to host

    cudaMemcpy(c, d_c, size, cudaMemcpyDeviceToHost);
    printf("Result:\n");
    for (int i = 0; i < n; i++) 
        printf("%d ", c[i]);

    printf("\n");

    // Cleanup
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
    return 0;

}