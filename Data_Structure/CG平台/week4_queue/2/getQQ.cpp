#include<iostream>
#include<queue>
using namespace std;

/* 设计算法string getQQ(string numbers) ，通过给定的数字串numbers和给定的规则，得出一个qq号。
规则如下：
首先将第1个数删除，接着将第2个数放到这串数的末尾，再将第3个数删除并将第4个数放到这串数的末尾，
再将第5个数删除……
直到剩下最后一个数，将最后一个数也删除。按照刚才删除的顺序，把这些删除的数连在一起就是我的QQ号。
如：给出的数字串是631758924，则返回的qq号是615947283。 */

string getQQ(string numbers)
{
    queue<char> qu1; //创建一个string类型的queue用于存放数字串
    queue<char> qu2;
    string string_QQ; //创建一个string用来存放QQ号
    for (int i = 0; i < numbers.size(); i++)
    {
        qu1.push(numbers[i]); //将numbers存放在queue中
    }
    while (qu1.size() > 1)
    {
        qu2.push(qu1.front());  //将删除的数放到qu2中
        qu1.pop();              //将第一个数删除          
        qu1.push(qu1.front());
        qu1.pop();              //将第二个数放在这串数的末尾
    }
    if (qu1.size() == 1)
    {
        qu2.push(qu1.front());
        qu1.pop(); //将最后一个数也删除
    }
    for (int i = 0; i < qu2.size(); i++) 
    {  
        string_QQ += (qu2.front());
        qu2.push(qu2.front());
        qu2.pop();
    }
    return string_QQ;
}

int main()
{
    string numbers;
    cin >> numbers;
    cout << getQQ(numbers) << endl;
    system("pause");
    return 0;
}