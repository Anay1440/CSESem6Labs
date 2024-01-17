#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[]) {

    int rank, size, n, count = 0;
    char str[100], recv_str[100];

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int * recv_count_arr = (int *) malloc(size * sizeof(int));

    if (rank == 0) {
        printf("Enter a string of length divisible by %d ", size);
        scanf("%s", str);
        n = strlen(str) / size;
    }

    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

    MPI_Scatter(str, n, MPI_CHAR, recv_str, n, MPI_CHAR, 0, MPI_COMM_WORLD);

    for (int i = 0; i < n; i++) {
        char ch = tolower(recv_str[i]);
        if (ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u')
            count++;
    }

    MPI_Gather(&count, 1, MPI_INT, recv_count_arr, 1, MPI_INT, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        count = 0;
        for (int i = 0; i < size; i++) {
            count += recv_count_arr[i];
            printf("Process with rank %d sent count: %d\n", i, recv_count_arr[i]);
        }
        printf("Final count: %d\n", count);
    }
    
    MPI_Finalize();
    return 0;
}