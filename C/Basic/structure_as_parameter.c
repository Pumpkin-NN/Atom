#include <stdio.h>


struct Rectangle{
  int length;
  int breath;
};

/*
//Call by Value Method
int area(struct Rectangle r1){
  r1.length++;
  return r1.length * r1.breath;
}
*/
//Call by Address
void changeLength(struct Rectangle *p, int l){
  p->length = l;
}

int main(){
  struct Rectangle r = {10, 5};
/*
  printf("%d\n", area(r));
  //Call by value does not change the actual values
  printf("%d\n%d\n", r.length, r.breath);
*/
  changeLength(&r, 20);
  printf("%d\n",r.length);

}
