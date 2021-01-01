#include<stdio.h>
#include <string.h>

FILE *fp;

int main() {
	fp = fopen("input", "r");

	fclose(fp);
	return 0;
}
