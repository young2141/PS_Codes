#include<iostream>
#include<fstream>
using namespace std;

//NFF(non increasing first fit) : off-line
//FF(first fit) : on-line -> flexible (tournament)

int objSize[100];
int tree[100];
int player[100];
int n, binCap, treeSize;

void printTree() {
	for (int i = 1; i < treeSize; i++)
		cout << tree[i] << " ";
	cout << " | ";
	for (int i = 1; i <= n; i++)
		cout << player[i] << " ";
	cout << "\n";
}

void init() {

	for (int k = 1; k <= treeSize; k = k + 2) {
		int p = (k + treeSize - 1) / 2;
		tree[p] = k;
	}

	for (int k = (treeSize - 1) / 2; k > 0; k--) {
		tree[k] = tree[k * 2];
	}
	for (int i = 1; i <= treeSize; i++)
		player[i] = binCap;
	printTree();
}

void binPacking() {
	for (int i = 1; i <= n; i++) {
		int bin = objSize[i];
		int pos = 1;

		while (pos < treeSize) {
			if (player[tree[pos]] >= bin)
				pos = pos * 2;
			else
				pos += 1;
		}
		pos = pos / 2;

		int node = 2 * pos - treeSize + 1;
		if (player[node] >= bin)
			player[node] -= bin;
		else
			player[node + 1] -= bin;

		if (player[node] > player[node + 1])
			tree[pos] = node;
		else
			tree[pos] = node + 1;

		while (pos > 1) {
			if (player[tree[pos / 2 * 2]] >= player[tree[pos / 2 * 2 + 1]])
				tree[pos / 2] = tree[pos / 2 * 2];
			else
				tree[pos / 2] = tree[pos / 2 * 2 + 1];
			pos = pos / 2;
		}

		printTree();
	}
}

int main() {

	ifstream fin("input.txt");
	fin >> binCap >> n >> treeSize; // n = number of input

	init();
	for (int i = 1; i <= n; i++)
		fin >> objSize[i];

	binPacking();	

	for (int i = 1; i <= n; i++)
		cout << player[i] << " ";
}
