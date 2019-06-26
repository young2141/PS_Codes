//n���� ����Ÿ n�� ����
//2,3  4,5  6,7  8,9 sorting
//1,2  3,4  5,6  7,8 sorting ..and so on 
//n���� CPU n�� sorting.(CPU�ϳ��� 1 ������) O(n^2)

//n*n 2���� �迭�� �����Ѵٸ�? 
// (1�ٿ��� row���� sorting(Ȧ�� ¦��). 0(n). �Ŀ�  n�ٸ�ŭ col���� sorting.O(n)) �� log n ��ŭ �ݺ� 
//. -->���� (nlog n) * n^2 = O(n^3 * log n )

//���� : 0,1�θ� �̷���� matrix���� �� : 
//row sorting�ϰ� col���� sorting ������ ��� n/2�� clean row ���ȴ�. ->log n�ϸ� �� row�� dirty.

#include<iostream>
#include<fstream>
#include<algorithm>
#include<cmath>
using namespace std;
int n;
int c[100][100];



void printGraph() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			printf("%5d", c[i][j]);
		puts("");
	}
	puts("");
}


void rightsort(int k)
{
	int i, j, temp;

	for (i = 0; i < n / 2; i++) {
		for (j = 1; j < n; j = j + 2) {
			int big = max(c[k][j - 1], c[k][j]);
			int small = min(c[k][j - 1], c[k][j]);

			c[k][j - 1] = small;
			c[k][j] = big;
		}

		for (j = 2; j < n; j = j + 2) {
			int big = max(c[k][j - 1], c[k][j]);
			int small = min(c[k][j - 1], c[k][j]);
			c[k][j - 1] = small;
			c[k][j] = big;
		}
	}
}



void leftsort(int k)
{
	int i, j, temp;

	for (i = 0; i < n / 2; i++) {
		for (j = 1; j < n; j = j + 2) {
			int big = max(c[k][j - 1], c[k][j]);
			int small = min(c[k][j - 1], c[k][j]);

			c[k][j - 1] = big;
			c[k][j] = small;
		}

		for (j = 2; j < n; j = j + 2) {
			int big = max(c[k][j - 1], c[k][j]);
			int small = min(c[k][j - 1], c[k][j]);
			c[k][j - 1] = big;
			c[k][j] = small;
		}
	}
}

void downsort(int k)
{
	int i, j, temp;

	for (i = 0; i < n / 2; i++) {
		for (j = 1; j < n; j = j + 2) {
			int big = max(c[j - 1][k], c[j][k]);
			int small = min(c[j-1][k], c[j][k]);

			c[j - 1][k] = small;
			c[j][k] = big;
		}

		for (j = 2; j < n; j = j + 2) {
			int big = max(c[j - 1][k], c[j][k]);
			int small = min(c[j-1][k], c[j][k]);

			c[j - 1][k] = small;
			c[j][k] = big;
		}
	}
}


void sort()
{
	int m = log2(ceil(n));
	int i, j, k, p;

	for (i = 0; i < m; i++) {
		for (j = 0; j < n; j++) {
			if (j % 2 == 0)
				rightsort(j);
			else
				leftsort(j);
		}
		printGraph();
		for (j = 0; j < n; j++)
			downsort(j);
		printGraph();
	}

	for (i = 0; i < n; i++)
		rightsort(i);
}

int main() {

	ifstream fin("input.txt");

	fin >> n;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			fin >> c[i][j];

	sort();
	printGraph();


}