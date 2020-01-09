#include <stdio.h>

// Output: 3 2 1
void func_recur1(n){
  if(n > 0){
    printf("%d\n", n);
    func_recur1(n-1);
  }
}

// Output: 1 2 3
void func_recur2(n){
  if(n > 0){
    func_recur2(n-1);
    printf("%d\n", n);
  }
}

int main(){
  int n = 3;
  //unc_recur1(n);
  func_recur2(n);
}
