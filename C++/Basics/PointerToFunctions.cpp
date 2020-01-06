#include<iostream>

using namespace std;

int max(int i, int j){
  return i>j?i:j;
}

int min(int i, int j){
  return i<j?i:j;
}

int main(){
  //Declear a pointer
  int (*fp)(int, int);
  int maximum, minimum;
  //Assign the pointer function
  //Point to the function max
  //function max is called
  fp = max;
  maximum = (*fp)(10, 5);
  printf("The max number is: %d\n", maximum);

  //Reassign the pointer function
  //Point to the function min
  //function min is called
  fp = min;
  minimum = (*fp)(30, 20);
  printf("The min number is: %d\n", minimum);
}

// Close to the polymorphism
