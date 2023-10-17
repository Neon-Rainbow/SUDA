#include<iostream>
#include<string>
#include<stack>
#include<algorithm>

using namespace std;

string stringdeal(string s)
{
	stack<char> x;
	x.push(s[0]);
	for (int i = 1; i < s.size(); i++)
	{

		if (s[i] == x.top())
			x.pop();
		else
			x.push(s[i]);
	}
	string s1 = "";
	while (x.size()!=0)
	{
		s1 += x.top();
		x.pop();
	}
	reverse(s1.begin(), s1.end());
	return s1;
}

int main()
{
	string s;
	cin >> s;
	cout << stringdeal(s);
	return 0;
}



