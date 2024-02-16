__kernel void vector_octal(__global int * A, __global int * B) {
    int octalNum[10];
    int i = get_global_id(0);
    int num = A[i], index = 0, res = 0;
    while (num != 0) {
        octalNum[index++] = num % 8;
        num = num / 8;
    }
    for (int j = index - 1; j >= 0; j--)
        res = res * 10 + octalNum[j];
    B[i] = res;
}