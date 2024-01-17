#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    int rank, size, n;
    char str1[100], str2[100], recv_str1[100], recv_str2[100];

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0) {
        printf("Enter a string of length divisible by %d ", size);
        scanf("%s", str1);
        fflush(stdin);
        printf("Enter another string of same length ");
        scanf("%s", str2);
        n = strlen(str1) / size;
    }

    MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);

    MPI_Scatter(str1, n, MPI_CHAR, recv_str1, n, MPI_CHAR, 0, MPI_COMM_WORLD);
    MPI_Scatter(str2, n, MPI_CHAR, recv_str2, n, MPI_CHAR, 0, MPI_COMM_WORLD);

    int flag = 1, ind1 = 0, ind2 = 0;
    for (int i = 0; i < 2 * n; i++) {
        if (flag)
            str1[i] =  recv_str1[ind1++];
        else
            str1[i] = recv_str2[ind2++];
        flag = 1 - flag;
    }
    str1[2 * n] = '\0';

    MPI_Gather(str1, 2 * n, MPI_CHAR, recv_str1, 2 * n, MPI_CHAR, 0, MPI_COMM_WORLD);

    if (rank == 0) 
        printf("Final string: %s\n", recv_str1);
    
    MPI_Finalize();
    return 0;
}