#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int up, down, height, day;
	scanf("%d %d %d", &up, &down, &height);

	if (height - up <= 0)
		day = 1;
	else {
		day = (height - up) / (up - down) + 1;
		if ((height - up) % (up - down))
			day++;
	}

	printf("%d", day);

	return 0;
}