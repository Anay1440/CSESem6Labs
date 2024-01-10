#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[]) {

    /*
        How to execute: 
        $ mpicc -o sample sample.c
        $ mpirun -n 16 ./sample
    */

    int rank, size;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    
    printf("My rank is %d in total %d processes\n", rank, size);
    MPI_Finalize();
    return 0;
}
