#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[]) {

    int rank, size;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Status status;

    if (rank == 0) {
        int n;
        printf("Enter number ");
        scanf("%d", &n);
        MPI_Send(&n, 1, MPI_INT, 1, 1, MPI_COMM_WORLD);
        MPI_Recv(&n, 1, MPI_INT, size - 1, 1, MPI_COMM_WORLD, &status);
        printf("Received %d in root process. Exiting.\n", n);
    }
    else {
        int n, toSend = (rank == size - 1) ? 0 : rank + 1;
        MPI_Recv(&n, 1, MPI_INT, rank - 1, 1, MPI_COMM_WORLD, &status);
        printf("Process with rank %d received: %d\n", rank, n);
        n += 1;
        MPI_Send(&n, 1, MPI_INT, toSend, 1, MPI_COMM_WORLD);
    }
    
    MPI_Finalize();
    return 0;
}
