#include<stdio.h>
#include<stdlib.h>
#pragma warning(disable:4996)

#define TRUE 1
#define FALSE 0

int n;
int col[60];
int got = 0;
FILE* fin;
FILE* fout;

int promising(int i) {
	int k = 1;
	int prom = TRUE;

	while (k < i && prom) {
		if (col[i] == col[k] || abs(col[i] - col[k]) == abs(i - k))
			prom = FALSE;
		k++;
	}
	return prom;
}

void queen(int i) {

	if (promising(i)) {
		if (i == n) {
			for (int j = 1; j <= i; j++)
				fprintf(fout,"%d\n", col[j]);
			exit(1);
		}
		else {			
			for (int j = 1; j <= n; j++) {
				col[i + 1] = j;
				queen(i + 1);
			}
		}
		
	}
}

int main() {

	char fname[50];
	printf("input file name? ");
	scanf("%s", fname);
	fin = fopen(fname, "r");
	fscanf(fin, "%d", &n);
	fout = fopen("output.txt", "w");
	queen(0);
}