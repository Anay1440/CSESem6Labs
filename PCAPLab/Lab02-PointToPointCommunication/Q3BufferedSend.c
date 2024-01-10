#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    int rank, size, n;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int buff[30]; // must be greater than 24
    MPI_Buffer_attach(&buff, sizeof(buff));

    if (rank == 0) {
        int * arr = (int *) malloc((size - 1) * sizeof(int));
        for (int i = 1; i < size; i++) {
            printf("Enter number ");
            scanf("%d", &arr[i - 1]);
        }
        for (int i = 1; i < size; i++)
            MPI_Bsend(&arr[i - 1], 1, MPI_INT, i, 1, MPI_COMM_WORLD);
    }
    else {
        MPI_Status status;
        int n;
        MPI_Recv(&n, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
        if (rank % 2 == 0) 
            printf("Process %d : %d\n", rank, (n * n));
        else
            printf("Process %d : %d\n", rank, (n * n * n));
    }
    int s = sizeof(buff);
    MPI_Buffer_detach(&buff, &s);
    MPI_Finalize();
    return 0;
}
