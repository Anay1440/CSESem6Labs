__kernel void vector_swap_adj(__global int * A) {
    int i = get_global_id(0) * 2;
    int temp = A[i + 1];
    A[i + 1] = A[i];
    A[i] = temp;
}