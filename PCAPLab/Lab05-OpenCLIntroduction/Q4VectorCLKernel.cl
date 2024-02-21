__kernel void vector_bin_to_dec(__global char * A, __global int * B) {
    int i = get_global_id(0);
    int lengthOfNumber = 4;
    int offset = i * lengthOfNumber;
    int res = 0;
    int val = 1;
    for (int k = 0; k < lengthOfNumber - 1; k++)
        val *= 2;
    for (int j = 0; j < lengthOfNumber; j++) {
        if (A[offset + j] == '1') {
            res += val;
        }
        val /= 2;
    }
    B[i] = res;
}