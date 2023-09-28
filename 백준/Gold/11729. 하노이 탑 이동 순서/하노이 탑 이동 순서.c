#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int fromArr[10000000];
int toArr[10000000];

void Hanoi(int n, int from, int mid, int to, int* count)
{
	if (n == 1) {
		fromArr[*count] = from;
		toArr[(*count)++] = to;
		return;
	}

	Hanoi(n - 1, from, to, mid, count);
	fromArr[*count] = from;
	toArr[(*count)++] = to;
	Hanoi(n - 1, mid, from, to, count);
}

int main()
{
	int n;
	scanf("%d", &n);

	int count = 0;
	Hanoi(n, 1, 2, 3, &count);

	printf("%d\n", count);
	for (int i = 0; i < count; ++i)
	{
		printf("%d %d\n", fromArr[i], toArr[i]);
	}

	return 0;
}