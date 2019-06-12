#include<stdio.h>
#include <stdlib.h>
#define MAX 99999999

FILE* fin;
FILE* fout;

int **w, **l;
char **t;


void init(int n) {

	w = (int**)malloc(sizeof(int*)*n); 
	l = (int**)malloc(sizeof(int*)*n);
	t = (char**)malloc(sizeof(char*)*n);
	for (int i = 0; i <= n+1; i++) {
		w[i] = (int*)malloc(sizeof(int)*n);
		l[i] = (int*)malloc(sizeof(int)*n);
		t[i] = (char*)malloc(sizeof(char)*n);
		for (int j = 0; j <= n + 1; j++) {
			w[i][j] = MAX;
			l[i][j] = MAX;
		}		
	}
}

void dijkstra(int n) {
	int ni = 0;
	int nj = 0;

	t[1][1] = '*';
	l[1][1] = 0;
	for (int count = 0; count < n *n; count++) {
		int min = MAX;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				if (l[i][j] >= 0 && l[i][j] < min) {
					min = l[i][j];
					ni = i; nj = j;
				}
		if (ni == n && nj == n) return;

		if (l[ni + 1][nj] != -1 && l[ni + 1][nj] == MAX) {
			l[ni + 1][nj] = l[ni][nj] + w[ni + 1][nj];
			t[ni + 1][nj] = 'U';

		}
		if (l[ni][nj + 1] != -1 && l[ni][nj + 1] == MAX) {
			l[ni][nj + 1] = l[ni][nj] + w[ni][nj + 1];
			t[ni][nj + 1] = 'L';

		}
		if (l[ni][nj - 1] != -1 && l[ni][nj - 1] == MAX) {
			l[ni][nj - 1] = l[ni][nj] + w[ni][nj - 1];
			t[ni][nj - 1] = 'R';
		}
		if (l[ni - 1][nj] != -1 && l[ni - 1][nj] == MAX) {
			l[ni - 1][nj] = l[ni][nj] + w[ni - 1][nj];
			t[ni - 1][nj] = 'D';

		}
		l[ni][nj] = -1;
	}
}

void path(int a, int b) {

	if (a == 1 && b == 1) {
		fprintf(fout,"1 1\n");
		return;
	}
	switch (t[a][b]) {
	case 'U': path(a - 1, b); break;
	case 'L': path(a, b - 1); break;
	case 'R': path(a, b + 1); break;
	case 'D': path(a + 1, b); break;
	default: return;
	}
	fprintf(fout,"%d %d\n", a, b);
}

int main() {

	int n;
	char c;
	char fname[50];
	printf("input file name? ");
	scanf("%s", fname);

	if ((fin = fopen(fname, "r")) == NULL) {
		printf("error : inputfile read fail");
		exit(1);
	}

	if ((fout = fopen("output.txt", "w")) == NULL) {
		printf("error: outputfile create fail");
		exit(1);
	}

	fin = fopen("input.txt", "r");
	fscanf(fin, "%d", &n);

	init(n);

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) {
			c = getc(fin);
			if (c == '\n')
				c = getc(fin);
			if (c == '0')
				w[i][j] = 1;
			else
				w[i][j] = 0;
		}

	dijkstra(n);
	fprintf(fout,"%d\n", l[n][n]);
	path(n, n);
	system("pause");
}