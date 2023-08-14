# include <stdio.h>
# define LEN 7 // 임의로 배열 길이를 정해서 저장함.

void quickSort(int arr[], int L, int R);

int main(){
  int i;
  int arr[LEN] = {5,1,6,3,4,2,7};
  printf("정렬 전 : ");
  for(i=0; i<LEN; i++){
    printf("%d ", arr[i]);
  }
  printf("\n");
    
  quickSort(arr, 0, LEN-1);
  
  printf("정렬 후 : ");
  for(i=0; i<LEN; i++){
    printf("%d ", arr[i]);
  }
  
  return 0; 
}


void quickSort(int arr[], int L, int R) {
      int left = L, right = R;
      int pivot = arr[(L + R) / 2];    // pivot 설정을 중간 값으로 함. 
      int temp;
      do
      {
        while (arr[left] < pivot)    // left가 pivot보다 큰 값을 만나거나 pivot을 만날 때까지 
            left++;
        while (arr[right] > pivot)    // right가 pivot보다 작은 값을 만나거나 pivot을 만날 때까지 
            right--;
        if (left<= right)    // left가 right보다 왼쪽에 있다면 교환 
        {
            temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            /*left 오른쪽으로 한칸, right 왼쪽으로 한칸 이동*/
            left++;
            right--;
        }
      } while (left<= right);    // left가 right 보다 오른쪽에 있을 때까지 반복 
 
    if (L < right)
        quickSort(arr, L, right);    // 왼쪽 배열 재귀 호출
 
    if (left < R)
        quickSort(arr, left, R);    // 오른쪽 배열 재귀 호출 
}
 
// 퀵정렬의 평균 시간 복잡도 : nlogn