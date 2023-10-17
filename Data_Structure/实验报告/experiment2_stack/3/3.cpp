#include <iostream>
#include <stack>
#include <sstream>
#include <fstream>
#include <map>

using namespace std;

int SignToInt(string sign) //将运算符号以及括号用int来表达
{
    if (sign == "+"){return -1;}
    else if (sign == "-"){return -2;}
    else if (sign == "*"){return -3;}
    else if (sign == "/"){return -4;}
    else if (sign == "("){return -5;}
    else if (sign == ")"){return -6;}
}

stack<double> infixExpression(string lst[], int n)
{
    stack<double> sign_stack; // sigh_stack用来存放符号
    stack<double> temp_stack; // temp_stack用来存放中间结果
    string operators1 = "+-*/";
    string operators2 = "+-*/" ;
    string brackets = "()";
    string left_bracket = "(";
    string right_bracket = ")";
    int i = 0;
    double num;
    while (i < n)
    {
        string m = lst[i];
        if (operators1.find(m) == string::npos) //判断第i个元素是否是运算符
        {                                         //无法在operators中找到m，说明第i个元素是数字，需要入栈
            istringstream iss(m);
            iss >> num;
            temp_stack.push(num);
        }
        else if (SignToInt(m) == -5) //判断第i个元素是否是左括号
        {                            //第i个元素为左括号
                                     //如果是左括号就直接压入sign_stack
            sign_stack.push(-5);
        }
        else if (SignToInt(m) == -6) //判断第i个元素是否是右括号
        {                            //第i个元素是右括号
                                     //如果是右括号，则依次弹出sign_stack的栈顶，将弹出的元素压入temp_stack，直到遇到右括号为止，并将这一对括号丢弃
            while (true)
            {
                if (sign_stack.top() != -6)
                {
                    temp_stack.push(sign_stack.top());
                    sign_stack.pop();
                }
                else
                {
                    sign_stack.pop();
                    break;
                }
            }
        }
        else if (operators2.find(m) != string::npos) //判断第i个元素是否是否是运算符
        {                                              //第i个元素是运算符
        Label1:;
            if (sign_stack.empty() or sign_stack.top() == -5)
            { // 1.若sign_stack为空，或者栈顶运算符为左括号，则直接入栈
                sign_stack.push(SignToInt(m));
            }
            else if ((SignToInt(m) == -3 or SignToInt(m) == -4) and (sign_stack.top() == -1 or sign_stack.top() == -2))
            { // 2.优先级高于栈顶运算符，也直接入栈
                sign_stack.push(SignToInt(m));
            }
            else
            { // 3.否则，将sigh_stack栈顶运算符弹出压入temp_stack，再转到步骤1进行判断
                temp_stack.push(sign_stack.top());
                sign_stack.pop();
                goto Label1;
            }
        }
        i += 1;
    }
    return temp_stack;
}

string InfixToPost(stack<double> st, string lst[]) //将中缀表达式转换为后缀表达式
{
    for(int i = 0;i<st.size();i++)
    {
        lst+=st.top();
        st.pop();
    }
}

double PostfixExpression(string lst[], int n)
{
    stack<double> st;
    string operators = "+-*/";
    int i = 0;
    double num;
    while (i < n)
    {
        string m = lst[i];
        if (operators.find(m) == string::npos) //判断第i个元素是否是表达式
        {                                      //无法在operators中找到m，说明第i个元素是数字，需要入栈
            istringstream iss(m);
            iss >> num;
            st.push(num);
        }
        else
        { //在operators中找到了m，说明第i个元素是运算符，需要计算
            double y = st.top();
            st.pop();
            double x = st.top();
            st.pop();
            double z;
            string temp_operators = m;
            if (temp_operators == "+")
            {
                z = x + y;
            }
            else if (temp_operators == "-")
            {
                z = x - y;
            }
            else if (temp_operators == "*")
            {
                z = x * y;
            }
            else if (temp_operators == "/")
            {
                z = x / y;
            }
            st.push(z);
        }
        i += 1;
    }
    return st.top();
}

int main()
{
    string infix_exression = "3.5 * ( 20 + 4 ) - 20 / 4"; //待计算的中缀表达式
    string infix_exression_array[20];                     //存放中缀表达式的字符串
    istringstream ss(infix_exression);
    int i = 0;
    while (ss >> infix_exression_array[i])
    {
        i++; // i为中缀表达式中的元素的数量,
    }
    cout << PostfixExpression(infix_exression_array, i) << endl;
    system("pause");
    return 0;
}