//n개의 데이타 n번 소팅
//2,3  4,5  6,7  8,9 sorting
//1,2  3,4  5,6  7,8 sorting ..and so on 
//n개의 CPU n번 sorting.(CPU하나당 1 데이터) O(n^2)

//n*n 2차원 배열로 연결한다면? 
// (1줄에서 row방향 sorting(홀수 짝수). 0(n). 후에  n줄만큼 col방향 sorting.O(n)) 을 log n 만큼 반복 
//. -->총합 (nlog n) * n^2 = O(n^3 * log n )

//증명 : 0,1로만 이루어진 matrix있을 때 : 
//row sorting하고 col방향 sorting 끝나면 적어도 n/2는 clean row 가된다. ->log n하면 한 row만 dirty.

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