#include <iostream>
using namespace std;

/*
class Calculate{
private:
  int m;
  int n;
public:
  Calculate(int a, int b);
  int Add();
  int Substruct();
};

Calculate::Calculate(int a, int b){
  m = a;
  n = b;
}

int Calculate::Add(){
  int c;
  c = m + n;
  return c;
}

int Calculate::Substruct(){
  int c;
  c = m - n;
  return c;
}


int main(){
  Calculate c(10,20);
  cout<<c.Add()<<endl;
  cout<<c.Substruct()<<endl;
}
*/

/*
//Use "this", "this" implies the current object
class Calculate{
private:
  int a;
  int b;
public:
  Calculate(int a, int b);
  int Add();
  int Substruct();
};

Calculate::Calculate(int a, int b){
  //Distinguish the a and b, use the keyword "this"
  //"this" is a pointer of the current object, implies its members
  this->a = a;
  this->b = b;
}

int Calculate::Add(){
  int c;
  c = a + b;
  return c;
}

int Calculate::Substruct(){
  int c;
  c = a - b;
  return c;
}


int main(){
  Calculate c(10,20);
  cout<<c.Add()<<endl;
  cout<<c.Substruct()<<endl;
}
*/


//Use Templates to work for any types of data
template<class T>
class Calculate{
private:
  T a;
  T b;
public:
  Calculate(T a, T b);
  T Add();
  T Substruct();
};

template<class T>
Calculate<T>::Calculate(T a, T b){
  //Distinguish the a and b, use the keyword "this"
  //"this" is a pointer of the current object, implies its members
  this->a = a;
  this->b = b;
}

template<class T>
T Calculate<T>::Add(){
  T c;
  c = a + b;
  return c;
}

template<class T>
T Calculate<T>::Substruct(){
  T c;
  c = a - b;
  return c;
}


int main(){
  Calculate<int> Ic(10,20);
  cout<<"Calculate the intergers"<<endl;
  cout<<Ic.Add()<<endl;
  cout<<Ic.Substruct()<<endl;

  Calculate<float> Fc(100.1100000,200.0);
  cout<<"Calculate the floats"<<endl;
  cout<<Fc.Add()<<endl;
  cout<<Fc.Substruct()<<endl;

}
