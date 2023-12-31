# include <stdio.h>
# define MAX_SIZE 8
int sorted[MAX_SIZE]; // 추가적인 공간이 필요

void merge(int list[], int left, int mid, int right);
void merge_sort(int list[], int left, int right);


void main(){
  int n = MAX_SIZE;
  int list[MAX_SIZE] = {21, 10, 12, 20, 25, 13, 15, 22};

  // 합병 정렬 수행(left: 배열의 시작 = 0, right: 배열의 끝 = 7)
  merge_sort(list, 0, n-1);

  // 정렬 결과 출력
  for(int i=0; i<n; i++){
    printf("%d\n", list[i]);
  }
}

void merge(int list[], int left, int mid, int right){
  int i, j, k, l;
  i = left; // i: 정렬된 왼쪽 리스트에 대한 인덱스
  j = mid+1; // j: 정렬된 오른쪽 리스트에 대한 인덱스
  k = left; // k: 정렬될 리스트에 대한 인덱스

  
  while(i<=mid && j<=right){ //분할 정렬된 list의 합병
    if(list[i]<=list[j])
      sorted[k++] = list[i++];
    else
      sorted[k++] = list[j++];
  }

  
  if(i>mid){ // 남아 있는 값들을 일괄 복사
    for(l=j; l<=right; l++)
      sorted[k++] = list[l];
  }
  else{ // 남아 있는 값들을 일괄 복사
    for(l=i; l<=mid; l++)
      sorted[k++] = list[l];
  }
  for(l=left; l<=right; l++){ // 배열 sorted[](임시 배열)의 리스트를 배열 list[]로 재복사
    list[l] = sorted[l];
  }
}

void merge_sort(int list[], int left, int right){ // 합병 정렬
  int mid;

  if(left<right){
    mid = (left+right)/2; // 중간 위치를 계산하여 리스트를 균등 분할 -분할(Divide)
    merge_sort(list, left, mid); // 앞쪽 부분 리스트 정렬 -정복(Conquer)
    merge_sort(list, mid+1, right); // 뒤쪽 부분 리스트 정렬 -정복(Conquer)
    merge(list, left, mid, right); // 정렬된 2개의 부분 배열을 합병하는 과정 -결합(Combine)
  }
}

// 2-way-merge의 평균 시간 복잡도 : nlogn