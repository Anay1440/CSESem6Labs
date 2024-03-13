#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

__global__ void conv(double *a, double *out) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    out[i] = sin(a[i]);
}

int main(void) {
    int n;

    printf("Enter n ");
    scanf("%d", &n);

    // Host copies of vectors a, mask, out
    double * a = (double *) malloc(n * sizeof(double));
    double * out = (double *) malloc(n * sizeof(double));

    // Setup input values
    printf("Enter input array\n");
    for (int i = 0; i < n; i++) {
        printf("Enter a[%d] ", i);
        scanf("%lf", &a[i]);
    }

    double *d_a, *d_out; // Device copies
    int size = n * sizeof(double);

    // Allocate space for device copies

    cudaMalloc((void **)&d_a, size);
    cudaMalloc((void **)&d_out, size);

    // Copy inputs to device

    cudaMemcpy(d_a, a, size, cudaMemcpyHostToDevice);

    // Launch kernel on GPU

    conv<<<1, n>>>(d_a, d_out);

    // Copy result back to host

    cudaMemcpy(out, d_out, size, cudaMemcpyDeviceToHost);
    printf("Result:\n");
    for (int i = 0; i < n; i++) 
        printf("%.2lf ", out[i]);

    printf("\n");

    // Cleanup
    cudaFree(d_a);
    cudaFree(d_out);
    return 0;

}