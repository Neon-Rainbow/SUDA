#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

/*
【问题描述】
使用已学的各种数据结构及基本操作，设计算法void reverseOdd(CirQueue<int>& sq) ，对参数所给
定的队列sq中的整数进行操作，将其中奇数的顺序进行逆置，偶数的顺序维持不变。例如，sq中队头至队
尾的元素为：(14, 13, 17, 8, 4, 10, 11, 4, 15, 18, 19)，调用reverseOdd后，则sq的内容变为：
(14, 19, 15, 8, 4, 10, 11, 4, 17, 18, 13)。
【输入形式】
第1行，一个整数n，表示队列中的元素个数
第2行，n个整数，以空格分隔，表示队列中从队头到队尾的元素
【输出形式】n个整数，以空格分隔，表示队列中从队头到队尾的元素
【样例输入】
6
1 2 3 4 5 6
【样例输出】
5 2 3 4 1 6 */
template <class Typle>
class CirQueue
{
public:
    vector<int> vt;
    void EnQueue(int i)
    {
        vt.push_back(i);
    }
    void PrintOut()
    {
        int temp_size = vt.size();
        for (int i = 0; i < temp_size; i++)
        {
            cout << vt[i] << " ";
        }
    }
    int size()
    {
        return vt.size();
    }
};


void reverseOdd(CirQueue<int> &sq)
{
    stack<int> temp_stack;
    // queue<int> temp_queue;
    for (int i = 0; i < sq.size(); i++)
    {
        if (sq.vt[i] % 2 != 0) //判断奇偶
        {
            temp_stack.push(sq.vt[i]); //奇数存放到stack中
        }
    }
    if (temp_stack.size() != 0) //判断stack是否为空
    {
        for (int i = 0; i < sq.size(); i++) //遍历奇数
        {
            if (sq.vt[i] % 2 != 0) //判断奇偶
            {
                sq.vt[i] = temp_stack.top(); //栈是LIFO，因此最后一个进入栈的元素(栈顶元素)要放在第一个位置
                temp_stack.pop();            //删除栈顶元素
            }
        }
    }
}

int main()
{

    int n, item;

    CirQueue<int> sq;

    cin >> n;

    for (int i = 0; i < n; i++)
    {

        cin >> item;

        sq.EnQueue(item);
    }

    reverseOdd(sq);

    sq.PrintOut();

    system("pause");

    return 0;
}