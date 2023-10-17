#include<iostream>
#include<stack>
#include<sstream>
#include<fstream>

using namespace std;

double PostfixExpression(string lst[],int n)
{
    stack<double> st;
    string operators = "+-*/";
    int i = 0;
    double num;
    while(i<n)
    {
        string m = lst[i];
        if(operators.find(m)==string::npos) //判断第i个元素是否是表达式
        {//无法在operators中找到m，说明第i个元素是数字，需要入栈
            istringstream iss(m); 
            iss >> num; 
            st.push(num);
        }
        else
        {//在operators中找到了m，说明第i个元素是运算符，需要计算
            double y = st.top(); st.pop();
            double x = st.top(); st.pop();
            double z;
            string temp_operators = m;
            if(temp_operators == "+"){z = x+y;}
            else if(temp_operators == "-"){z = x-y;}
            else if(temp_operators == "*"){z = x*y;}
            else if(temp_operators == "/"){z = x/y;}
            st.push(z);
        }
        i+=1;
    }
    return st.top();
}


int main()
{
    string postfix_exression = "3.5 20 4 + * 20 4 / - "; //待计算的后缀表达式
    string postfix_exression_array[20]; //存放后缀表达式的字符串
    istringstream ss(postfix_exression);
    int i = 0;
    while(ss>>postfix_exression_array[i])
    {
        i++; //i为后缀表达式中的元素的数量,
    }
    /*
    cout<<"输入的后缀表达式为"<<postfix_exression<<endl;
    cout<<"计算结果为:";
    */
    cout<<PostfixExpression(postfix_exression_array,i)<<endl;
    system("pause");
    return 0;
}