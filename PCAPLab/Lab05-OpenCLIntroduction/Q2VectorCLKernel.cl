__kernel void vector_ones_complement(__global char * A, __global char * B) {
    int i = get_global_id(0);
    int lengthOfNumber = 4;
    int offset = i * lengthOfNumber;
    for (int j = 0; j < lengthOfNumber; j++) 
        B[offset + j] = (A[offset + j] == '0' ? '1' : '0');
}