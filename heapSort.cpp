#include<iostream>
#pragma warning(disable:4996)
using namespace std;

struct heap {
	int S[100];
	int heapsize;
};

void siftdown(int i, heap* H) {
	int siftkey = H->S[i];
	int parent = i; int smallerchild;
	bool found = false;

	while ((parent * 2 <= H->heapsize) && (!found)) {
		if (H->S[2 * parent] > H->S[2 * parent + 1])
			smallerchild = 2 * parent + 1;
		else
			smallerchild = 2 * parent;

		if (siftkey < H->S[smallerchild]) {
			H->S[parent] = H->S[smallerchild];
			parent = smallerchild;
		}
		else
			found = true;
	}
	H->S[parent] = siftkey;
}

void makeheap(heap* H) {
	for (int i = (H->heapsize / 2); i >= 1; i--)
		siftdown(i, H);
}

int main() {
	heap* H;
	H = (heap*)malloc(sizeof(heap));
	FILE* fin;
	fin = fopen("input.txt", "r");
	int i = 1;
	H->heapsize = 0;
	while (!feof(fin)) {
		fscanf(fin, "%d", &(H->S[i]));
		i++;
		H->heapsize++;
	}
	H->heapsize--;
	makeheap(H);

	for (int i = 1; i <= H->heapsize; i++)
		cout << H->S[i] << " ";
	system("pause");

}