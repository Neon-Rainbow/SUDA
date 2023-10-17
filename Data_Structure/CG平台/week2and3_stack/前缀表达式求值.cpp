#include<iostream>
#include<string>
#include<stack>
#include<sstream>
#include<algorithm>

using namespace std;


double prefix(string p[], int h)
{
    stack<double> x;
    for (int i = h - 1; i >= 0; i--)
    {
        if (!(p[i] == "*" || p[i] == "+" || p[i] == "-" || p[i] == "/"))
        {
            x.push(stod(p[i]));
        }
        else
        {
            if (x.empty() || x.size() == 1)
            {
                cout << "illegal expression" << endl;
                exit(0);
            }
            double a = x.top();
            x.pop();
            double b = x.top();
            double c;
            x.pop();
            if (p[i] == "+") c = a + b;
            else if (p[i] == "-") c = a - b;
            else if (p[i] == "*") c = a * b;
            else if (p[i] == "/") c = a / b;
            x.push(c);
        }

    }
    if (x.size() != 1)
    {
        cout << "illegal expression" << endl;
        exit(0);
    }
    return x.top();
}

int main() {

    string prefix_ex;

    getline(cin, prefix_ex);

    string prefix_array[20];

    stringstream ss(prefix_ex);

    int i = 0;

    while (ss >> prefix_array[i])

        i++;
        cout << prefix(prefix_array, i) << endl;

}




