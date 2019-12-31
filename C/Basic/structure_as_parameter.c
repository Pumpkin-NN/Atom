#include <stdio.h>

struct Rectangle{
  int length;
  int breath;
};

int area(struct Rectangle r1){
  r1.length++;
  return r1.length * r1.breath;
}

int main(){
  struct Rectangle r = {10, 5};
    printf("%d\n", area(r));
    printf("%d\n%d\n", r.length, r.breath);
}
