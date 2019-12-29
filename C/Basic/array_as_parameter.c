#include <stdio.h>
#include <stdlib.h>

#define SIZE 5
/*
// "int arr[]" is a actually a pointer(call by address), n is an integer(call by value)
// The pointer can modify the actual parameters in main func
void func(int arr[], int n) {
  for(int i = 0; i < n; i++){
    arr[0] = 10;
    printf("%d\n", arr[i]);
  }
}

int main(){
  int arr[5] = {2,3,4,5,1};
  func(arr, 5);
  return 0;
}
*/

// Return an array
int* func(int n){
  int *p;
  p = (int*)malloc(n*sizeof(int));
  printf("Insert some Elements in array, located in the heap memory: \n");
  for(int i = 0; i < n; i++){
    p[i] += i;
    printf("%d\n", p[i]);
  }

  free(p); // free malloc
  return p;
}

int main(){
  int *A;
  A = func(SIZE);
  printf("Rewrite the previous Elements in array, located in the heap memory: \n");
  for(int i = 0; i < SIZE; i++){
    // Rewrite the value from heap
    *A += 2;
    printf("%d\n", *A);
  }
}
