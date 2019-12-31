#include <iostream>
using namespace std;

struct Rectangle{
  int length;
  int breath;
};

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


int area(struct Rectangle &r1){
  r1.length++;
  return r1.length * r1.breath;
}

int main(){
  int a = 10;
  int b = 20;
  swap(a, b);
  printf("Passing parameters by REFERENCES, actual changed the actual parameters\n");
  printf("%d\n%d\n",a, b);

  printf("Structure as parameters: \n");
  struct Rectangle r = {10,5};
  printf("%d\n", area(r));
  printf("%d\n%d\n", r.length, r.breath);

}
