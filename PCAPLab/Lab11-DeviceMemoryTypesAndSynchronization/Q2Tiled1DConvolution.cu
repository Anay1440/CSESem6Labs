#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>

#define TILE_WIDTH 4
#define MAX_MASK_WIDTH 20

__constant__ int mask_constant_mem[100];

__global__ void conv(int *a, int *out, int *width, int * mask_width) {
    int n = *mask_width / 2;
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    int res = 0;
    
    __shared__ int shared_arr[TILE_WIDTH + MAX_MASK_WIDTH - 1];

    int halo_index_left = (blockIdx.x - 1) * blockDim.x + threadIdx.x;
    int halo_index_right = (blockIdx.x + 1) * blockDim.x + threadIdx.x;

    if (threadIdx.x >= blockDim.x - n)
        shared_arr[threadIdx.x - (blockDim.x - n)] = (halo_index_left >= 0) ? a[halo_index_left] : 0;

    if (threadIdx.x < n)
        shared_arr[threadIdx.x + blockDim.x + n] = (halo_index_right < *width) ? a[halo_index_right] : 0;

    shared_arr[n + threadIdx.x] = a[i];

    __syncthreads();

    for (int j = 0; j < *mask_width; j++)
        res += shared_arr[threadIdx.x + j] * mask_constant_mem[j];

    out[i] = res;
}

int main(void) {
    int n, m;

    printf("Enter n and m ");
    scanf("%d %d", &n, &m);

    // Host copies of vectors a, mask, out
    int * a = (int *) malloc(n * sizeof(int));
    int * mask = (int *) malloc(m * sizeof(int));
    int * out = (int *) malloc(n * sizeof(int));

    // Setup input values
    printf("Enter input array\n");
    for (int i = 0; i < n; i++) {
        printf("Enter a[%d] ", i);
        scanf("%d", &a[i]);
    }

    printf("Enter mask array\n");
    for (int i = 0; i < m; i++) {
        printf("Enter mask[%d] ", i);
        scanf("%d", &mask[i]);
    }

    int *d_a, *d_out, *d_width, *d_mask_width; // Device copies of vectors a, mask, out, width, mask_width
    int size = n * sizeof(int);
    int mask_size = m * sizeof(int);

    // Allocate space for device copies

    cudaMalloc((void **)&d_a, size);
    cudaMalloc((void **)&d_out, size);
    cudaMalloc((void **)&d_width, sizeof(int));
    cudaMalloc((void **)&d_mask_width, sizeof(int));

    // Copy inputs to device

    cudaMemcpy(d_a, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_width, &n, sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_mask_width, &m, sizeof(int), cudaMemcpyHostToDevice);

    // Method 1 to copy to constant memory:

    cudaMemcpyToSymbol(mask_constant_mem, mask, mask_size, 0, cudaMemcpyHostToDevice);

    // Launch kernel on GPU


    dim3 grid_conf(((n - 1) / TILE_WIDTH) + 1, 1, 1);
    dim3 block_conf(TILE_WIDTH, 1, 1);

    conv<<<grid_conf, block_conf>>>(d_a, d_out, d_width, d_mask_width);

    // Copy result back to host

    cudaMemcpy(out, d_out, size, cudaMemcpyDeviceToHost);
    printf("Result:\n");
    for (int i = 0; i < n; i++) 
        printf("%d ", out[i]);

    printf("\n");

    // Cleanup
    cudaFree(d_a);
    cudaFree(d_out);
    cudaFree(d_mask_width);
    return 0;

}