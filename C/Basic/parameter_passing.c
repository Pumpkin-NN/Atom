#include <stdio.h>
/*
//Passing parameters by values

void swap(int x, int y){
  int hold = x;
  x = y;
  y = hold;
  printf("Swapping the formal parameters\n");
  printf("%d\n%d\n",x, y);
}

int main(){
  int a = 10;
  int b = 20;
  swap(a, b);
  printf("Passing parameters by values won't change the actual parameters\n");
  printf("%d\n%d\n",a, b);
}
*/

// The method above is not actually suitable for the swap function
// Use the call by Address, using pointers
void swap(int *x, int *y){
  int hold = *x;
  *x = *y;
  *y = hold;
}

int main(){
  int a = 10;
  int b = 20;
  swap(&a, &b);
  printf("Passing parameters by Address, modifying the actual parameters\n");
  printf("%d\n%d\n",a, b);
}
