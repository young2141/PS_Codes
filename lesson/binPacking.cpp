#pragma warning(disable:4996)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILE_MAX 255

void initial();
void push(int);

int *arr;
int *tree;
int n, max_size, count;

int main()
{

	int size;
	int i;

	char file_name[FILE_MAX];

	FILE *fp;

	printf("input file : ");
	scanf("%s", file_name);

	fp = fopen(file_name, "r");

	fscanf(fp, "%d %d %d ", &n, &count, &max_size);

	arr = (int *)malloc(sizeof(int)*(n + 1));
	tree = (int *)malloc(sizeof(int) * n);
	//memset(arr, 20, sizeof(int)*(n + 1));
	memset(tree, 0, sizeof(int) * n);

	for (i = 1; i <= n; i++)
		arr[i] = max_size;

	initial();
	for (i = 0; i < count; i++)
	{
		fscanf(fp, "%d ", &size);
		push(size);
	}

	for (i = 1; i <= n; i++)
		printf("%d ", arr[i]);

	printf("\n");
	system("pause");
}

void initial()
{
	int k;
	int p;

	for (k = 1; k <= n; k = k + 2)
	{
		p = (k + n - 1) / 2;

		/*if (arr[k] >= arr[k + 1])
			tree[p] = k;
		else
			tree[p] = k + 1;*/
		tree[p] = k;
	}

	for (k = (n - 1) / 2; k > 0; k--)
	{
		/*if (arr[tree[k * 2]] >= arr[tree[k * 2 + 1]])
			tree[k] = tree[k * 2];
		else
			tree[k] = tree[k * 2 + 1];*/
		tree[k] = tree[k * 2];
	}
	for (int i = 1; i <= n; i++)
		printf("%d ", tree[i]);
}

void push(int size)
{
	int find;
	int head = 1;
	int p;

	// 집어넣을 장소 찾기
	while (head <= (n - 1) / 2)
	{
		if (arr[tree[head * 2]] >= size)
			head = head * 2;
		else
			head = head * 2 + 1;
	}



	//값 집어넣기
	if (tree[head] % 2 != 0) // 홀수
	{
		if (arr[tree[head]] >= size) {
			arr[tree[head]] = arr[tree[head]] - size;
			find = tree[head];
		}
		else {
			arr[tree[head] + 1] = arr[tree[head] + 1] - size;
			find = tree[head] + 1;
		}
	}

	else // 짝수
	{
		if (arr[tree[head] - 1] >= size) {
			arr[tree[head] - 1] = arr[tree[head] - 1] - size;
			find = tree[head] - 1;
		}
		else {
			arr[tree[head]] = arr[tree[head]] - size;
			find = tree[head];
		}
	}


	// 위로 올라가면서 갱신
	p = (find + n - 1) / 2;

	if (find % 2 != 0) // 홀수
	{
		if (arr[find] >= arr[find + 1])
			tree[p] = find;
		else
			tree[p] = find + 1;
	}
	else
	{
		if (arr[find - 1] >= arr[find])
		{
			tree[p] = find - 1;
		}
		else
			tree[p] = find;
	}

	while (p != 1)
	{
		if (p % 2 != 0) // 홀수
		{
			if (arr[tree[p - 1]] >= arr[tree[p]])
				tree[p / 2] = tree[p - 1];
			else
				tree[p / 2] = tree[p];
		}
		else {
			if (arr[tree[p]] >= arr[tree[p + 1]])
				tree[p / 2] = tree[p];
			else
				tree[p / 2] = tree[p + 1];
		}
		p = p / 2;
	}
}