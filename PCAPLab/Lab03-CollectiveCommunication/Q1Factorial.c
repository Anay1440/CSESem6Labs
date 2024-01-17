#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    int rank, size, num, fact = 1;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int * arr = (int *) malloc(size * sizeof(int));
    if (rank == 0) {
        for (int i = 0; i < size; i++) {
            printf("Enter number ");
            scanf("%d", &arr[i]);
        }
    }
    MPI_Scatter(arr, 1, MPI_INT, &num, 1, MPI_INT, 0, MPI_COMM_WORLD);

    for (int i = 1; i <= num; i++)
        fact = fact * i;
    printf("Process with rank %d received %d and sending: %d\n", rank, num, fact);
    MPI_Gather(&fact, 1, MPI_INT, arr, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        int sum = 0;
        for (int i = 0; i < size; i++)
            sum += arr[i];
        printf("Final sum: %d", sum);
    }
    
    MPI_Finalize();
    return 0;
}