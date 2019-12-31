#include <iostream>
using namespace std;


class Rectangle{
private:
  int length;
  int breath;
public:
  Rectangle(int l, int b){
    length = l;
    breath = b;
  }

  int getLength(){
    return length;
  }
  int area(){
    return length * breath;
  }

  void changeLength(int l){
    length = l;
  }
};


int main(){
  Rectangle r(10,5);

  int area;

  area = r.area();

  printf("The orignal area is %d\n", area);

  r.changeLength(20);

  printf("The length is %d\n", r.getLength());

  area = r.area();

  printf("The new area is %d\n", area);
}
