#include<iostream>
#include<string>
#include<stack>
#include<algorithm>

using namespace std;

void detach(int n)
{
	cout << n << "=";
	stack<int> x;
	for (int i = 2; i <= n; i++)
	{
		while (n % i == 0)
		{
			x.push(i);
			n /= i;
		}
	}
	cout << x.top();
	x.pop();
	while (!x.empty())
	{
		cout<<"*" << x.top();
		x.pop();
	}
}

int main()
{
	int n;
	cin >> n;
	detach(n);
}



