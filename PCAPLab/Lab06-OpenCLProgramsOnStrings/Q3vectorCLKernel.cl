__kernel void vector_brick_sort_odd_step(__global int * A, __constant int * len) {
    int i = get_global_id(0) * 2 + 1;
    int lengthOfArray = * len;
    if (((i + 1) < lengthOfArray) && (A[i] > A[i + 1])) {
        int temp = A[i];
        A[i] = A[i + 1];
        A[i + 1] = temp;
    }
}

__kernel void vector_brick_sort_even_step(__global int * A, __constant int * len) {
    int i = get_global_id(0) * 2;
    int lengthOfArray = * len;
    if (((i + 1) < lengthOfArray) && (A[i] > A[i + 1])) {
        int temp = A[i];
        A[i] = A[i + 1];
        A[i + 1] = temp;
    }
}