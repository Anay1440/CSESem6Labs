#include <mpi.h>
#include <stdio.h>

int main(int argc, char *argv[]) {

    char * input = "-5 + 7";

    MPI_Init(&argc, &argv);
    
    int rank, op1 = 0, op2 = 0, n = 0, negativeNum = 0;
    char operator = '\0';

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    while(input[n] != '\0') {
        if (operator == '\0') {
            if (input[n] >= '0' && input[n] <= '9')
                op1 = op1 * 10 + input[n] - '0';
            else if (input[n] == '-' && op1 == 0)
                negativeNum = 1;
            else if (input[n] == '+' || input[n] == '-' || input[n] == '*' || input[n] == '/') {
                operator = input[n];
                if (negativeNum)
                    op1 = -op1;
                negativeNum = 0;
            }
        }
        else {
            if (input[n] >= '0' && input[n] <= '9')
                op2 = op2 * 10 + input[n] - '0';
            else if (input[n] == '-' && op2 == 0)
                negativeNum = 1;
            if (input[n + 1] == '\0')
                if (negativeNum)
                    op2 = -op2;
        }
        n++;
    }

    int val = 0;

    if (operator == '+' && rank == 0) {
        val = op1 + op2;
        printf("Value: %d\n", val);
    }
    else if (operator == '-' && rank == 1) {
        val = op1 - op2;
        printf("Value: %d\n", val);
    }
    else if (operator == '*' && rank == 2) {
        val = op1 * op2;
        printf("Value: %d\n", val);
    }
    else if (operator == '/' && rank == 3) {
        val = op1 / op2;
        printf("Value: %d\n", val);
    }
    
    MPI_Finalize();
    return 0;
}
