#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
struct link {
	int vertex;
	int time;
	link* next;
	link* end;
};
int n,fixfree;
link** node;
int W[100];
int T[100];
int D[100];
int P[100];
int station_num = 0;

void countpath(int v)
{
	station_num++;
	if (P[v] == 0) {
		printf("%d\n", station_num - 1);
		return;	}
	countpath(P[v]);
}

void path(int v) {
	if (P[v] == 0)
		return;
	path(P[v]);
	printf("%d ",P[v]);
}

int main() {
	ifstream fin("input.txt");
	fin >> fixfree;
	fin >> n;
	node = new link*[n + 2];
	for (int i = 0; i <= n + 1; i++) {
		node[i] = new link;
		node[i]->next = NULL;
		node[i]->end = NULL;
	}
	for (int i = 1; i <= n+1; i++) {
		fin >> W[i];
	}	
	for (int i = 1; i <= n; i++)
		fin >> T[i];
	for (int i = 0; i <= n; i++) {
		int cur_dist = 0; int check = i+1;
		while (true) {
			if (cur_dist + W[check] <= fixfree){
				if (check > n + 1)
					break;
				cur_dist += W[check];
				link* in = new link;
				in->time = T[check];
				in->vertex = check++;
				in->next = NULL; in->end = NULL;
				if (node[i]->next == NULL) {
					node[i]->next = in;
					node[i]->end = in;
				}
				else {
					node[i]->end->next = in;
					node[i]->end = in;
				}				
			}
			else
				break;
		}
	}
	fill(D, D + 100, 987654321);
	D[0] = 0;
	for(int i=0;i<=n+1;i++)
		for (link* j = node[i]->next; j != NULL; j = j->next) {
			if (D[j->vertex] > D[i] + j->time) {
				D[j->vertex] = D[i] + j->time;
				P[j->vertex] = i;
			}
		}
	printf("d : ");
	for (int i = 0; i <= n + 1; i++)
		printf("%d ", D[i]);
	puts("");
	printf("p: ");
	for (int i = 0; i <= n + 1; i++)
		printf("%d ", P[i]);

	printf("\n\n");
	printf("%d\n", D[n + 1]);
	countpath(n + 1);
	path(n+1);
	puts("");

	system("pause");
}