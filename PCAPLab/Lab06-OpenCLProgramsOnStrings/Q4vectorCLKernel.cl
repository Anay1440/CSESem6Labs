__kernel void vector_rev_each_word(__global char * A, __constant int * lengths) {
    int i = get_global_id(0);
    int lengthOfWord = lengths[i];
    int offset = 0;
    for (int j = 0; j < i; j++) {
        offset += lengths[j];
    }
    int left = offset, right = offset + lengthOfWord - 1;
    while (left < right) {
        char ch = A[left];
        A[left] = A[right];
        A[right] = ch;
        left++;
        right--;
    }
}