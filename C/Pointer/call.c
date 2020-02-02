# include <stdio.h>
# include <stdlib.h>


void printHW(){
  printf("HelloWorld\n");
}

int *Add(int *a, int *b){
  *a = *a + 1;
  *b = *b + 1;
  int *c = (int*)malloc(sizeof(int));
  *c = *a + *b;
  free(c);
  return c;
}


int main(){
  int a = 2;
  int b = 4;

  int *c = Add(&a, &b);
  printHW();
  printf("%d\n%d\n%d\n", a, b, *c);



}
