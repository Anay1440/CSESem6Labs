#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    int rank, size, m, arr[100], recv_arr[100];
    float avg = 0;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    float * recv_avg_arr = (float *) malloc(size * sizeof(float));

    if (rank == 0) {
        printf("Enter value of m ");
        scanf("%d", &m);
        for (int i = 0; i < m * size; i++) {
            printf("Enter number ");
            scanf("%d", &arr[i]);
        }
    }

    MPI_Bcast(&m, 1, MPI_INT, 0, MPI_COMM_WORLD);

    MPI_Scatter(arr, m, MPI_INT, recv_arr, m, MPI_INT, 0, MPI_COMM_WORLD);

    for (int i = 0; i < m; i++)
        avg += (float) recv_arr[i] / m;

    printf("Process with rank %d sending: %f\n", rank, avg);

    MPI_Gather(&avg, 1, MPI_FLOAT, recv_avg_arr, 1, MPI_FLOAT, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        avg = 0;
        for (int i = 0; i < size; i++)
            avg += recv_avg_arr[i] / size;
        printf("Final avg: %f\n", avg);
    }
    
    MPI_Finalize();
    return 0;
}