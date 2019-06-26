#include<iostream>
#include<sstream>
#include<cstring>
#include<fstream>
#include<string>
#include<set>
#include<vector>
#include<algorithm>


using namespace std;

int main() {
	int n, m; int answer = 0; string a;
	cin >> n >> m;
	set<string> words;
	vector<string> answers;

	for (int i = 0; i < n; i++) {
		cin >> a;
		words.insert(a);
	}
	for (int i = 0; i < m; i++) {
		cin >> a;
		if (words.find(a) != words.end()) {
			answer++;
			answers.push_back(a);
		}
	}
	cout << answer << endl;
	sort(answers.begin(), answers.end());
	for (auto i = answers.begin(); i != answers.end(); i++)
		cout << *i << endl;

}
