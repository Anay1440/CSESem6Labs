#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[]) {

    int rank, size;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0) {
        int n;
        printf("Enter number ");
        scanf("%d", &n);
        for (int i = 1; i < size; i++)
            MPI_Send(&n, 1, MPI_INT, i, 1, MPI_COMM_WORLD);
    }
    else {
        MPI_Status status;
        int n;
        MPI_Recv(&n, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
        printf("Process with rank %d received: %d\n", rank, n);
    }
    
    MPI_Finalize();
    return 0;
}
