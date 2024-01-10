#include <mpi.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    int rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Status status;

    if (rank == 0) {
        char word[50], ch;
        printf("Enter word ");
        scanf("%s", word);
        int wordLen = strlen(word);
        MPI_Ssend(&wordLen, 1, MPI_INT, 1, 1, MPI_COMM_WORLD);
        MPI_Ssend(word, wordLen, MPI_CHAR, 1, 1, MPI_COMM_WORLD);
        MPI_Recv(word, wordLen, MPI_CHAR, 1, 1, MPI_COMM_WORLD, &status);
        printf("Final word: %s\n", word);
    }
    else {
        int wordLen;
        MPI_Recv(&wordLen, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
        char * word = (char *) malloc(wordLen * sizeof(char)), ch;
        MPI_Recv(word, wordLen, MPI_CHAR, 0, 1, MPI_COMM_WORLD, &status);
        for (int i = 0; i < wordLen; i++) {
            if (isupper(word[i]))
                word[i] = tolower(word[i]);
            else
                word[i] = toupper(word[i]);
        }
        MPI_Ssend(word, wordLen, MPI_CHAR, 0, 1, MPI_COMM_WORLD);
    }
    
    MPI_Finalize();
    return 0;
}