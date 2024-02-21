__kernel void vector_selection_sort(__global int * A, __constant int * len, __global int * B) {
    int i = get_global_id(0);
    int curr = A[i];
    int count = 0; // count number of elements that the current element is greater than
    int lengthOfArray = * len;
    for (int j = 0; j < lengthOfArray; j++) {
        if (curr > A[j])
            count++;
    }
    B[count] = curr;
}