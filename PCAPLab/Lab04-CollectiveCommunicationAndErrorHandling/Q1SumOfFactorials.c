#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    int rank, size, num, fact = 1, ans, errcode;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    MPI_Errhandler_set(MPI_COMM_WORLD, MPI_ERRORS_RETURN);

    int * arr = (int *) malloc(size * sizeof(int));
    if (rank == 0) {
        for (int i = 0; i < size; i++) {
            printf("Enter number ");
            scanf("%d", &arr[i]);
        }
    }
    errcode = MPI_Scatter(arr, 1, MPI_INT, &num, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if (errcode != MPI_SUCCESS) {
        char errorString[50]; int len;
        MPI_Error_string(errcode, errorString, &len);
        printf("Error. %s\n", errorString);
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    for (int i = 1; i <= num; i++)
        fact = fact * i;

    errcode = MPI_Scan(&fact, &ans, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);

    if (errcode != MPI_SUCCESS) {
        char errorString[50]; int len;
        MPI_Error_string(errcode, errorString, &len);
        printf("Error. %s\n", errorString);
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    if (rank == size - 1) {
        printf("Final sum: %d", ans);
    }
    
    MPI_Finalize();
    return 0;
}