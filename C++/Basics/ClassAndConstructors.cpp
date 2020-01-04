#include <iostream>
using namespace std;

class Rectangle{
private:
  int length;
  int breath;
public:
  //Initialize Constructor, take no parameters
  Rectangle(){
    length = breath = 1;
  }
  //Overloaded Constructor, users set the parameters
  Rectangle(int l, int b){
    length = l;
    breath = b;
  }

  //Facilitors Prototypes
  int area();
  int perimeter();

  //Accessors/Getters
  int getLength(){
    return length;
  }
  int getBreath(){
    return breath;
  }

  //Mutators/Setters
  void setLength(int l){
    length = l;
  }

  void setBreath(int b){
    breath = b;
  }

  //Destroytor prototype
  ~Rectangle();
};



// Class Functions
//"::" is the Scope Resolution Operator
int Rectangle::area(){
  return length * breath;
}

int Rectangle::perimeter(){
  return 2*(length+breath);
}

//The Destroytor
Rectangle::~Rectangle(){

}
int main(){
  Rectangle r;

  cout<<"The Initialized Rectangle: \n";
  cout<<r.area()<<endl;
  cout<<r.perimeter()<<endl;

  r.setLength(6);
  r.setBreath(10);
  cout<<"Change the length and breath Rectangle: \n";
  cout<<r.getLength()<<endl;
  cout<<r.getBreath()<<endl;
  cout<<"Updated Rectangle: \n";
  cout<<r.area()<<endl;
  cout<<r.perimeter()<<endl;

  Rectangle r1(10,4);
  cout<<"Overloaded the Constructor: \n";
  cout<<r1.area()<<endl;
  cout<<r1.perimeter()<<endl;

  Rectangle r2(13,10);
  cout<<"Overloaded the Constructor again: \n";
  cout<<r2.area()<<endl;
  cout<<r2.perimeter()<<endl;
}
