#include<iostream>
#pragma warning(disable:4996)
using namespace std;

struct set {
	int vertex;
	int distance;
};

struct heap {
	set** S;
	int heapsize;
};

struct link {
	int vertex;
	int weight;
	link* end;
	link* next;
};
heap* H;
link** head;

void siftdown(int i, heap* H) {
	int siftkey = H->S[i]->distance;
	set* temp = new set;
	temp->distance = siftkey; temp->vertex = H->S[i]->vertex;
	int parent = i; int smallerchild;
	bool found = false;

	while ((parent * 2 <= H->heapsize) && (!found)) {
		if (H->S[2 * parent]->distance > H->S[2 * parent + 1]->distance)
			smallerchild = 2 * parent + 1;
		else
			smallerchild = 2 * parent;

		if (siftkey > H->S[smallerchild]->distance) {
			H->S[parent] = H->S[smallerchild];
			parent = smallerchild;
		}
		else
			found = true;
	}
	H->S[parent] = temp;
}

void makeAdj(int from, int to,int weight) {

	link* in = new link;
	in->vertex = to; in->next = NULL;
	in->weight = weight; in->end = NULL;

	if (head[from]->next == NULL) {
		head[from]->next = in;
		head[from]->end = in;
	}
	else {
		head[from]->end->next = in;
		head[from]->end = in;
	}

	link* in2 = new link;
	in2->vertex = from; in2->next = NULL;
	in2->weight = weight; in2->end = NULL;

	if (head[to]->next == NULL) {
		head[to]->next = in2;
		head[to]->end = in2;
	}
	else {
		head[to]->end->next = in2;
		head[to]->end = in2;
	}

}

void makeheap(heap* H) {
	for (int i = (H->heapsize / 2); i >= 1; i--)
		siftdown(i, H);
}

void printgraph(int vertex) {
	for (int i = 1; i <= vertex; i++) {
		for (link* temp = head[i]->next; temp != NULL; temp = temp->next) {
			printf("(%d %d %d) ", i, temp->vertex, temp->weight);
		}
		puts("");
	}
}

int extract_min()
{
	int keyout = H->S[1]->vertex;

	H->S[1] = H->S[H->heapsize];
	H->heapsize = H->heapsize - 1;
	siftdown(1,H);

	return keyout;
}

void insert(int ver, int dis) {
	/*H->S[H->heapsize+1]->distance = dis;
	H->S[H->heapsize+1]->vertex = ver;
	H->heapsize += 1;
	makeheap(H);*/

	
	H->heapsize += 1;
	int i= H->heapsize;
	

	while ((i > 1) && (dis < H->S[i/2]->distance))
	{
	H->S[i] = H->S[i/2];
	
	i= i / 2;
	}
	set* temp = new set;
	temp->distance = dis;
	temp->vertex = ver;
	
	H->S[i] = temp;
}

int flag[100];
int d[100];
int p[100];


void mst_prim(int vertex, int r) {
	for(int i = 1;i<=vertex;i++)
		 {
			d[i] = 987654321; flag[i] = 0;
		}
	d[r] = 0; p[r] = -1;
	insert(r, d[r]);
	while (H->heapsize != 0) {
		int u = extract_min();
		if (flag[u] == 0) {
			for (link* temp = head[u]->next; temp != NULL; temp = temp->next) {
				int v = temp->vertex;
				if (flag[v] == 0 && temp->weight < d[v]) {
					p[v] = u;
					d[v] = temp->weight;
					insert(v, d[v]);
				}
			}
			flag[u] = 1;
		}
		for (int i = 1; i <= H->heapsize; i++) {
			printf("%d ", H->S[i]->distance);
		}
		puts("");
	}

}

int main() {
	
	H = (heap*)malloc(sizeof(heap));
	FILE* fin;
	fin = fopen("input.txt", "r");
	int vertex, edge,weight;
	H->S = new set*[100];
	for (int i = 0; i < 100; i++)
		H->S[i] = new set;
	H->heapsize = 0;
	fscanf(fin, "%d%d", &vertex, &edge);
	head = new link*[vertex+1];
	for (int i = 1; i <= vertex; i++) {
		head[i] = new link;
		head[i]->next = NULL; head[i]->end = NULL;
	}
	int to, from;
	for (int i = 1; i <= edge; i++) {
		fscanf(fin, "%d%d%d", &from, &to,&weight);
		makeAdj(from, to,weight);
	}
	printgraph(vertex);

	mst_prim(vertex, 1);

	int dist = 0;

	printf("\nnearest: ");
	for (int i = 1; i <= vertex; i++) {
		printf("%d ", p[i]);
		dist += d[i];
	}
	puts("");
	printf("total weight : %d\n", dist);
	system("pause");

}