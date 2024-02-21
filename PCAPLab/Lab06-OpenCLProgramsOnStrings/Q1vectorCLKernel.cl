__kernel void vector_copy_str(__global char * A, __constant int * len, __global char * B) {
    int i = get_global_id(0);
    int lengthOfString = * len;
    int offset = i * lengthOfString;
    for (int j = 0; j < lengthOfString; j++) 
        B[offset + j] = A[j];
}