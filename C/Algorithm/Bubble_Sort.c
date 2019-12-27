#include <stdio.h>

#define SIZE 12

int main(){
  int arr[SIZE] = {3,2,1,3,1,2,4,6,8,5,3,5};

  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE-1; j++){
      if (arr[j] > arr[j+1]){
        int hold = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = hold;
      }
    }
  }

  for(int k = 0; k < SIZE; k++){
    printf("%d\n", arr[k]);
  }


}
