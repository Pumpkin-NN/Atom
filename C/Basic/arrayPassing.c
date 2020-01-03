#include <stdio.h>


int Sum(int A[], int n){
  int s = 0;
  for(int i=0; i<n; i++){
    s = s + A[i];
  }
  //printf("%d\n", s);
  return s;
}

int main(){
  int s;
  int A[] = {2,4,5,3,2};
  s = Sum(A, 5);
  printf("%d\n", s);
}
