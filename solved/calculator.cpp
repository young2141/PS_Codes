#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <sstream>
#include <stack>
using namespace std;

struct oper
{
	int p;
	string o;
};

vector<oper> toPostOrder(stringstream& ss)
{
	stack<oper> op;
	string tok;
	stack<oper> post;
	while (ss >> tok)
	{
		if (tok == "(")
			op.push({ 0, tok });
		else if (tok == ")") {
			while (op.top().o != "(")
			{
				post.push(op.top());
				op.pop();
			}
			op.pop();
		}
		else if (tok == "*" || tok == "/" || tok == "+" || tok == "-")
		{
			int prior = 0;
			if (tok == "*")
				prior = 2;
			else if (tok == "/")
				prior = 2;
			else if (tok == "+")
				prior = 1;
			else if (tok == "-")
				prior = 1;
			while (!op.empty() && prior <= op.top().p)
			{
				post.push(op.top());
				op.pop();
			}
			op.push({ prior, tok });
		}
		else
			post.push({ -1,tok });
	}
	while (!op.empty())
	{
		post.push(op.top());
		op.pop();
	}

	vector<oper>rev;
	while(!post.empty())
	{
		rev.insert(rev.begin(),post.top());
		post.pop();
	}

	return rev;
}

int calc(vector<oper> post)
{
	int a, b,result;
	char op;
	stack<int> s;
	for(auto i=0;i<post.size();++i)
	{
		if (post[i].p == -1) {
			s.push(stoi(post[i].o));
		}
		else{
			b = s.top();
			s.pop();
			a = s.top();
			s.pop();
			op = post[i].o[0];
			switch (op)
			{
			case '*': result = a * b; break;
			case '/': result = a / b; break;
			case'+': result = a + b; break;
			case'-': result = a - b; break;
			}
			s.push(result);
		}
	}
	return s.top();
}

int main()
{
	string input = "15 + 32 * ( 1 - 8 ) / 2";
	stringstream ss(input);
	vector<oper> post = toPostOrder(ss);
	//for (auto p : post)
	//	cout << p.o << " ";
	cout << calc(post) << endl;		
	return 0;
}
