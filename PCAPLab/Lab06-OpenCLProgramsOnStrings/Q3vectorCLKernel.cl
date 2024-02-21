__kernel void vector_brick_sort_odd_step(__global int * A) {
    int i = get_global_id(0) * 2 + 1;
    if (A[i] < A[i + 1]) {
        int temp = A[i];
        A[i] = A[i + 1];
        A[i + 1] = temp;
    }
}

__kernel void vector_brick_sort_even_step(__global int * A) {
    int i = get_global_id(0) * 2;
    if (A[i] < A[i + 1]) {
        int temp = A[i];
        A[i] = A[i + 1];
        A[i + 1] = temp;
    }
}