#include <iostream>
using namespace std;

//References do not take any memory
//It is the another name for other variables
//In this case, the alias for the main function variables
void swap(int &x, int &y){
  int hold = x;
  x = y;
  y = hold;
  printf("Swapping the formal parameters, as REFERENCES of the actual parameters\n");
  printf("%d\n%d\n",x, y);
}

int main(){
  int a = 10;
  int b = 20;
  swap(a, b);
  printf("Passing parameters by REFERENCES, actual changed the actual parameters\n");
  printf("%d\n%d\n",a, b);
}
