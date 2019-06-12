#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
#pragma warning(disable:4996)
enum status { WHITE = 0, GRAY, BLACK };
#define INF 987654321
#define NIL -1
struct link {
	int vertex;
	int capacity;
	int flow;
	link* shadow;
	link* next;
};
struct head {
	link* front;
	link* rear;
};
struct Q {
	int val;
	Q* front;
	Q* rear;
	Q* next;
};
head **V;
Q* queue;
int color[100];
int d[100];
int p[100];
int totFlow = 0;

void ENQUEUE(int x) {
	Q*in = (Q*)malloc(sizeof(Q));
	in->val = x; in->front = NULL; in->next = NULL; in->rear = NULL;
	if (queue->front == NULL) {
		queue->front = in;
		queue->rear = in;
		queue->next = in;
	}
	else {
		queue->rear->next = in;
		queue->rear = in;
	}
}

Q* DEQUEUE() {
	Q*temp = (Q*)malloc(sizeof(Q));
	temp = queue->front;
	queue->front = queue->front->next;
	return temp;
}

bool EMPTYQUEUE() {
	if (queue->front == NULL)
		return true;
	else
		return false;
}

void BFS(int s) {
	for (int i = 0; i < 100; i++) {
		color[i] = WHITE;
		d[i] = INF; p[i] = NIL;
	}	
	color[s] = GRAY; d[s] = 0; p[s] = -1;
	ENQUEUE(s);
	while (!EMPTYQUEUE()) {
		int u = queue->front->val;
		for (link* temp = V[u]->front; temp != NULL; temp = temp->next) {
			int v = temp->vertex;
			if ((color[v] == WHITE) && (temp->flow >= 0) && (temp->capacity - temp->flow > 0)) {
				color[v] = GRAY; d[v] = d[u] + 1;
				p[v] = u; ENQUEUE(v);
			}
		}
		DEQUEUE();
		color[u] = BLACK;	
	}
}

void init(int vertex) {
	V = (head**)malloc(sizeof(head*));
	for (int i = 0; i <= vertex + 1; i++) {
		V[i] = (head*)malloc(sizeof(head));
		V[i]->front = NULL; V[i]->rear = NULL;
	}
	queue = (Q*)malloc(sizeof(Q));
	queue->front = NULL; queue->rear = NULL; queue->next = NULL;
	
}

void makeAdj(int from, int to, int cap) {
	link* node = (link*)malloc(sizeof(link));
	node->vertex = to;
	node->capacity = cap;
	node->flow = 0;
	node->next = NULL; node->shadow = NULL;

	link* shadow = (link*)malloc(sizeof(link));
	shadow->vertex = from;
	shadow->capacity = 0;
	shadow->flow = 0;
	shadow->next = NULL; shadow->shadow = node;
	node->shadow = shadow;
	bool find = false;
	if (V[from]->front == NULL) {
		V[from]->front = node;
		V[from]->rear = node;
	}
	else {

		for (link* temp = V[from]->front; temp != NULL; temp = temp->next) {
			if (temp->vertex == to) {
				temp->capacity = cap; find = true;
			}
		}
		if (!find) {
			V[from]->rear->next = node;
			V[from]->rear = node;
		}
	}

	if (V[to]->front == NULL) {
		V[to]->front = shadow;
		V[to]->rear = shadow;
	}
	else
		if (!find) {
			V[to]->rear->next = shadow;
			V[to]->rear = shadow;
		}
}

void printGraph(int vertex) {
	for (int u = 0; u <= vertex + 1; u++) {
		printf("%d : ", u);
		for (link* temp = V[u]->front; temp != NULL; temp = temp->next) {
			printf("(%d %d %d) ", temp->vertex, temp->capacity, temp->flow);
		}
		puts("");
	}


}


void flowIn(head* P) {
	int choice = INF;
	for (link* temp = P->front; temp != NULL; temp = temp->next) {
		choice = min(choice, temp->shadow->capacity - temp->shadow->flow);
	}
	printf("flow : %d", choice);
	totFlow += choice;
	for (link* temp = P->front; temp != NULL; temp = temp->next) {
		temp->shadow->flow += choice;
		temp->shadow->shadow->flow -=  choice;
	}

}
void makeP(int x, head* P) {	

	if (p[x] == -1) {
		flowIn(P);
		return;
	}

	link* node = (link*)malloc(sizeof(link));
	node->next = NULL;
	for (link* temp = V[p[x]]->front; temp != NULL; temp = temp->next)
		if (temp->vertex == x) {
			node->shadow = temp;
			node->vertex = x;
		}

	if (P->front == NULL) {
		P->front = node; P->rear = node;
	}

	else {
		node->next = P->front;
		P->front = node;
	}
	makeP(p[x],P);
}

int main() {
	FILE* fin;
	fin = fopen("input.txt", "r");
	int edge, vertex;
	fscanf(fin, "%d%d", &vertex, &edge);
	int from, to, cap;
	init(vertex);
	for (int i = 0; i < edge; i++) {
		fscanf(fin, "%d%d%d", &from, &to, &cap);
		makeAdj(from, to, cap);
	}

	printGraph(vertex);
	
	while (true) {
		head* P;
		P = (head*)malloc(sizeof(head));
		P->front = NULL; P->rear = NULL;
		BFS(0);
		if (p[vertex + 1] == -1)
			break;
		printf("\np :");
		for (int i = 0; i <= vertex + 1; i++)
			printf("%d ", p[i]);
		makeP(vertex + 1,P);
	}
	printf("\nMax Flow is : %d\n", totFlow);
	system("pause");
	return 0;
}