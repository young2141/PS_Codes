#include<stdio.h>
#include<stdlib.h>

#define MAX 9999999

int **EEL, **DDL, **PPL;
int **EER, **DDR, **PPR;
int *W, *D;

FILE* fin;
FILE* fout;

void init(int n, int m) {

	EEL = (int**)malloc(sizeof(int**)*n);
	DDL = (int**)malloc(sizeof(int**)*n);
	PPL = (int**)malloc(sizeof(int**)*n);
	EER = (int**)malloc(sizeof(int**)*n);
	DDR = (int**)malloc(sizeof(int**)*n);
	PPR = (int**)malloc(sizeof(int**)*n);
	D = (int*)malloc(sizeof(int)*n);
	W = (int*)malloc(sizeof(int)*n);

	for (int i = 1; i <= n; i++) {
		EEL[i] = (int*)malloc(sizeof(int*) * n);
		DDL[i] = (int*)malloc(sizeof(int*) * n);
		PPL[i] = (int*)malloc(sizeof(int*) * n);
		EER[i] = (int*)malloc(sizeof(int*) * n);
		DDR[i] = (int*)malloc(sizeof(int*) * n);
		PPR[i] = (int*)malloc(sizeof(int*) * n);
	}
	for (int i = 1; i <= n; i++) {
		memset(EEL[i], 0, sizeof(int*) * (n + 1));
		memset(EER[i], 0, sizeof(int*) * (n + 1));
		memset(DDL[i], 0, sizeof(int*) * (n + 1));
		memset(DDR[i], 0, sizeof(int*) * (n + 1));
		memset(PPL[i], 0, sizeof(int*) * (n + 1));
		memset(PPR[i], 0, sizeof(int*) * (n + 1));
	}
	memset(W, 0, sizeof(int*) * (n + 1));
	memset(D, 0, sizeof(int*) * (n + 1));

}

void street(int n, int m) {

	for (int i = 1; i <= n; i++)
		EEL[i][i] = EER[i][i] = MAX;

	EEL[m][m] = EER[m][m] = 0;

	for (int dig = 1; dig <= n - 1; dig++)
		for (int l = 1; l <= n - dig; l++) {
			int r = l + dig;

			if ((EEL[l + 1][r] + (DDL[l + 1][r] + D[l + 1] - D[l])*W[l]) <
				(EER[l + 1][r] + (DDR[l + 1][r] + D[r] - D[l])*W[l]))
			{
				EEL[l][r] = EEL[l + 1][r] + (DDL[l + 1][r] + D[l + 1] - D[l])*W[l];
				DDL[l][r] = DDL[l + 1][r] + D[l + 1] - D[l];
				PPL[l][r] = l + 1;
			}
			else {
				EEL[l][r] = EER[l + 1][r] + (DDR[l + 1][r] + D[r] - D[l])*W[l];
				DDL[l][r] = DDR[l + 1][r] + D[r] - D[l];
				PPL[l][r] = r;
			}
			if ((EER[l][r - 1] + W[r] * (DDR[l][r - 1] + D[r] - D[r - 1])) <
				(EEL[l][r - 1] + W[r] * (DDL[l][r - 1] + D[r] - D[l])))
			{
				EER[l][r] = EER[l][r - 1] + W[r] * (DDR[l][r - 1] + D[r] - D[r - 1]);
				DDR[l][r] = DDR[l][r - 1] + D[r] - D[r - 1];
				PPR[l][r] = r - 1;
			}
			else {
				EER[l][r] = EEL[l][r - 1] + W[r] * (DDL[l][r - 1] + D[r] - D[l]);
				DDR[l][r] = DDL[l][r - 1] + D[r] - D[l];
				PPR[l][r] = l;
			}
		}
}

void printLight(int l, int r) {

	if (l == r)
		return;

	if (EEL[l][r] < EER[l][r]) {
		printLight(l + 1, r);
		fprintf(fout, "%d\n", PPL[l][r]);
	}
	else {
		printLight(l, r - 1);
		fprintf(fout, "%d\n", PPR[l][r]);
	}
}

int main() {
	int N, M;
	char fname[50];
	printf("input file name? ");
	gets(fname);


	if ((fin = fopen(fname, "r")) == NULL) {
		printf("error : inputfile read fail");
		exit(1);
	}

	if ((fout = fopen("output.txt", "w")) == NULL) {
		printf("error: outputfile create fail");
		exit(1);
	}


	fscanf(fin, "%d%d", &N, &M);

	init(N, M);

	for (int i = 1; i <= N; i++)
		fscanf(fin, "%d%d", &D[i], &W[i]);

	street(N, M);


	if (EEL[1][N] < EER[1][N]) {
		fprintf(fout, "%d\n", EEL[1][N]);
		printLight(1, N);
		fprintf(fout, "1\n");
	}
	else {
		fprintf(fout, "%d\n", EER[1][N]);
		printLight(1, N);
		fprintf(fout, "%d\n", N);
	}
}
