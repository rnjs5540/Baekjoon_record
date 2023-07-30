#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#define True 1
#define False 0

int main()
{
	int usedCount[26] = { 0 };
	char str[1000000];
	scanf("%s", str);

	int stringLength = strlen(str);
	for (int i = 0; i < stringLength; ++i)
	{
		if (str[i] > 96)
			usedCount[str[i] - 32 - 'A']++;
		else
			usedCount[str[i] - 'A']++;
	}

	int mostUsedIndex = 0;
	int isSameUsedExist = False;
	for (int i = 1; i < 26; ++i)
	{
		if (usedCount[mostUsedIndex] == usedCount[i])
			isSameUsedExist = True;
		else if (usedCount[mostUsedIndex] < usedCount[i]) {
			mostUsedIndex = i;
			isSameUsedExist = False;
		}
	}

	if (isSameUsedExist)
		printf("?");
	else
		printf("%c", 'A' + mostUsedIndex);

	return 0;
}