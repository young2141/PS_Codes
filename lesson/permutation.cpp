#include<iostream>
#include<algorithm>>
#include<string>
using namespace std;

void perm(string S, int k, int n) {

	if (k >= n) {
		cout << S << endl;
		return;
	}
	sort(S.begin()+k, S.end());
	perm(S, k + 1, n);
	sort(S.begin() + k + 1, S.end());

	for (int m = 1; m <= n; m++)
		if (m > k && S[m] > S[k]) {
			swap(S[m], S[k]);
			perm(S, k+1, n);
			sort(S.begin() + k + 1, S.end());
		}
}

int main() {

	string S = "caaabba";

	perm(S,1, S.size());
	system("pause");
}