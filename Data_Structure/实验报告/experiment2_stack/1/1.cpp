//（1）实现顺序栈类并测试正确性；
#include<iostream>
#include<vector>

using namespace std;

const int stack_size = 20;
template<typename DataType>
class SeqStack
{
public:
    SeqStack();
    ~SeqStack();
    void Push(DataType x);
    DataType Pop();
    DataType GetTop();
    int Empty();
private:
    DataType data[stack_size];
    int top; //栈顶的下标
}


void Seqstack<Datatype>::Push(Datatype x)
{
    if(top == stack_size-1){throw "stackoverflow";} //判断stack是否上溢
    else{data[top++] = x;}
}

Datatype SeqStack<Datatype>::pop()
{
    if(top == -1){throw"stackoverflow";} //判断stack是否下溢
    else{x = data[top--];return x;} //弹出stack的栈顶元素
}

Datatype Seqstack<Datatype>::GetTop()
{
    if(top == -1){throw"stackoverflow";} //判断stack是否下溢
    else{return data[top];}
}

int Seqstack::Empty()
{
    if(top == -1){return 0;}
    else{return 1;}
}
