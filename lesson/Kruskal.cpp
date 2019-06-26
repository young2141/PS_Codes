#include<iostream>
#include<fstream>
using namespace std;

struct way {
	int from;
	int to;
	int weight;
};

way **E;
way **F;

int parent[100];

void weightedUnion(int i, int j) {
	int size = parent[i] + parent[j];

	if (parent[i] > parent[j]) {
		parent[i] = j;
		parent[j] = size;
	}
	else {
		parent[j] = i;
		parent[i] = size;
	}
}

int collapsingFind(int i) {
	int r = i;
	for (; parent[r] >= 0; r = parent[r]);
	while (i != r) {
		int s = parent[i];
		parent[i] = r;
		i = s;
	}
	return r;
}

void initWay(int edge) {
	E = new way*[edge+1];
	F = new way*[edge+1];

	for (int i = 0; i <= edge; i++) {
		E[i] = new way;
		F[i] = new way;
	}
}

void kruskal(int n) {

	memset(parent, -1, sizeof(parent));
	int Fcount = 0;
	int e = 0;
	while(Fcount != n-1) {
		int i, j,w;
		i = E[e]->from;
		j = E[e]->to;
		w = E[e]->weight;
		int p = collapsingFind(i);
		int q = collapsingFind(j);
		if (p != q) {
			weightedUnion(p,q);
			F[Fcount]->from = i;
			F[Fcount]->to = j;
			F[Fcount++]->weight= w;
		}
		e++;
	}
}

void printResult(int vertex) {
	for (int i = 0; i < vertex - 1; i++)
		cout << F[i]->from << " " << F[i]->to << " " << F[i]->weight << endl;
}

int main() {

	ifstream fin("input.txt");
	int vertex, edge;
	fin >> vertex >> edge;
	initWay(edge);
	int to, from, weight;
	for (int i = 0; i < edge; i++) {
		fin >> from >> to >> weight;
		E[i]->from = from; E[i]->to = to; E[i]->weight = weight;		
	}
		
	kruskal(vertex);
	printResult(vertex);		
	system("pause");
}