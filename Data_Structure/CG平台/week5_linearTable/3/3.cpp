#include<iostream>

using namespace std;

template<typename DataType>
struct Node
{
    DataType data;
    Node<DataType>* next;
};

template<typename DataType>
class LinkList
{
public:
    LinkList();
    LinkList(DataType a[], int n);
    void reverse();
    void PrintList();
private:
    Node<DataType>* first;
};

template<typename DataType>
LinkList<DataType>::LinkList()
{
    first = new Node<DataType>;
    first->next = nullptr;
}

template<typename DataType>
LinkList<DataType>::LinkList(DataType a[], int n)
{
    first = new Node<DataType>;
    Node<DataType>* r = first, * s = nullptr;
    for (int i = 0; i < n; i++)
    {
        s = new Node<DataType>;
        s->data = a[i];
        r->next = s;
        r = s;
    }
    r->next = nullptr;
}



template<typename DataType>
void LinkList<DataType>::reverse()
{
    Node<DataType>* temp = nullptr, * q = nullptr;
    temp = first->next;
    first->next = nullptr;
    q = temp->next;
    while (temp!=nullptr)
    {
        temp->next = first->next;
        first->next = temp;
        temp = q;
        if (q!=nullptr)
        {
            q = q->next;
        }
    }
}

template<typename DataType>
void LinkList<DataType>::PrintList()
{
    Node<DataType>* p = first->next;
    while (p != nullptr)
    {
        cout << p->data << " ";
        p = p->next;
    }
    cout << endl;
}

int main()
{
    int n, r[100] = {};
    cin >> n;
    if (n > 0)
    {
        for (int i = 0; i < n; i++)
            cin >> r[i];
    }
    else
    {
        return 0;
    }
    LinkList<int>L{ r,n };
    L.reverse();
    L.PrintList();
    system("pause");
    return 0;
}