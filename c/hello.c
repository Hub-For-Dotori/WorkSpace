#include<stdio.h>
#include<stdlib.h>

#define MAX 1000;

int main(void) {
	int oddsum=0, in;
	char name[11];

	printf("이름 정수[1000이하] 입력:");
	scanf_s("%s %d", name, &in);

	for (int i = 1; i <= in; i++) {
		if (i % 2 == 0) {
			oddsum += i;
		}
	}

	printf("결과 : %s %d\n", name, oddsum);

	return 0;
}
// c or c++ : ctrl+alt+c => c or c++ selection => ctrl+alt+r => execute
//https://jhnyang.tistory.com/430
