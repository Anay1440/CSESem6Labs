#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>
#include <stdlib.h>

__global__ void mat_mult_row_wise(int * a, int * b, int * c, int wa, int wb) {
    int row_a = threadIdx.x;
    for (int col_b = 0; col_b < wb; col_b++) {
        int sum = 0;
        for (int k = 0; k < wa; k++)
            sum += (a[row_a * wa + k] * b[k * wb + col_b]);

        c[row_a * wb + col_b] = sum;
    }
}

__global__ void mat_mult_col_wise(int * a, int * b, int * c, int wa, int ha) {
    int col_b = threadIdx.x;
    int wb = blockDim.x;
    for (int row_a = 0; row_a < ha; row_a++) {
        int sum = 0; 
        for (int k = 0; k < wa; k++)
            sum += (a[row_a * wa + k] * b[k * wb + col_b]);

        c[row_a * wb + col_b] = sum;
    }
}

__global__ void mat_mult_ele_wise(int * a, int *b, int * c, int wa) {
    int row_a = threadIdx.x;
    int col_b = blockIdx.x;
    int wb = gridDim.x;
    int sum = 0;
    for (int k = 0; k < wa; k++)
        sum += (a[row_a * wa + k] * b[k * wb + col_b]);

    c[row_a * wb + col_b] = sum;
}

int main() {

    int r1, r2, c1, c2, * d_a, * d_b, * d_c;

    // User Input

    // printf("Enter dimensions of first matrix ");
    // scanf("%d %d", &r1, &c1);
    // printf("Enter dimensions of second matrix ");
    // scanf("%d %d", &r2, &c2);

    // if (c1 != r2) {
    //     printf("Matrices with given dimensions cannot be multiplied\n");
    //     exit(1);
    // }

    // printf("Enter input for matrix 1:\n");
    // int * mat1 = (int *) malloc(sizeof(int) * r1 * c1);
    // for (int i = 0; i < r1; i++) {
    //     for (int j = 0; j < c1; j++) {
    //         printf("Enter mat1[%d][%d] ", i, j);
    //         scanf("%d", &mat1[i * c1 + j]);
    //     }
    // }

    // printf("Enter input for matrix 2:\n");
    // int * mat2 = (int *) malloc(sizeof(int) * r2 * c2);
    // for (int i = 0; i < r2; i++) {
    //     for (int j = 0; j < c2; j++) {
    //         printf("Enter mat2[%d][%d] ", i, j);
    //         scanf("%d", &mat2[i * c2 + j]);
    //     }
    // }

    // Hardcoded input

    r1 = 1, c1 = 3, r2 = 3, c2 = 4;

    int mat1[] = {3, 4, 2};
    int mat2[] = {13, 9, 7, 15, 8, 7, 4, 6, 6, 4, 0, 3};

    // End of input

    printf("Mat1:\n");
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c1; j++) {
            printf("%d ", mat1[i * c1 + j]);
        }
        printf("\n");
    }

    printf("Mat2:\n");
    for (int i = 0; i < r2; i++) {
        for (int j = 0; j < c2; j++) {
            printf("%d ", mat2[i * c2 + j]);
        }
        printf("\n");
    }

    int * res = (int *) malloc(sizeof(int) * r1 * c2);

    cudaMalloc((void **)&d_a, r1 * c1 * sizeof(int));
    cudaMalloc((void **)&d_b, r2 * c2 * sizeof(int));
    cudaMalloc((void **)&d_c, r1 * c2 * sizeof(int));

    cudaMemcpy(d_a, mat1, r1 * c1 * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, mat2, r2 * c2 * sizeof(int), cudaMemcpyHostToDevice);

    // mat_mult_row_wise<<<1, r1>>>(d_a, d_b, d_c, c1, c2);

    // cudaMemcpy(res, d_c, r1 * c2 * sizeof(int), cudaMemcpyDeviceToHost);

    // printf("Result from rowwise:\n");

    // for (int i = 0; i < r1; i++) {
    //     for (int j = 0; j < c2; j++)
    //         printf("%d ", res[i * r1 + j]);
    //     printf("\n");
    // }

    // mat_mult_col_wise<<<1, c2>>>(d_a, d_b, d_c, c1, r1);

    // cudaMemcpy(res, d_c, r1 * c2 * sizeof(int), cudaMemcpyDeviceToHost);

    // printf("Result from columnwise:\n");

    // for (int i = 0; i < r1; i++) {
    //     for (int j = 0; j < c2; j++)
    //         printf("%d ", res[i * r1 + j]);
    //     printf("\n");
    // }

    mat_mult_ele_wise<<<c2, r1>>>(d_a, d_b, d_c, c1);

    cudaMemcpy(res, d_c, r1 * c2 * sizeof(int), cudaMemcpyDeviceToHost);

    printf("Result from elementwise:\n");

    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++)
            printf("%d ", res[i * c1 + j]);
        printf("\n");
    }

    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
    return 0;
}