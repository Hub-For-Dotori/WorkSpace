/*
연봉 계산기 lab1
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    int ysalary;
    int msalary;
    printf("연봉을 입력하시오(단위: 만원): ");
    scanf_s("%d", &ysalary);
    msalary = ysalary / 12;
    printf("월수령액(단위: 만원): %d", msalary);
    return 0;
}
