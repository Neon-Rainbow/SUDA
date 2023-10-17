// Different_set_of_seqlist.cpp: 定义应用程序的入口点。
//

#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<algorithm>

using namespace std;

template<typename DataType>
struct Node {
    DataType data;
    Node<DataType>* next;
};

template<typename DataType>
class LinkList {
public:
    LinkList();

    LinkList(DataType a[], int n);

    void Reverse();

    void PrintList();

    DataType Get(int i);

    int Empty();

    int Length();

    int Locate(DataType x);

    void Insert(int i, DataType x);

    //Node<DataType>* GetFirst();

    Node<DataType>* first;
};

template<typename DataType>
LinkList<DataType>::LinkList() {
    first = new Node<DataType>;
    first->next = nullptr;
}

template<typename DataType>
LinkList<DataType>::LinkList(DataType* a, int n) {
    first = new Node<DataType>;
    Node<DataType>* r = first, * s = nullptr;
    for (int i = 0; i < n; i++) {
        s = new Node<DataType>;
        s->data = a[i];
        r->next = s;
        r = s;
    }
    r->next = nullptr;
}

template<typename DataType>
void LinkList<DataType>::PrintList() {
    Node<DataType>* p = first->next;
    while (p != nullptr) {
        std::cout << p->data << " ";
        p = p->next;
    }
    std::cout << std::endl;
}

template<typename DataType>
DataType LinkList<DataType>::Get(int i) {
    Node<DataType>* p = first->next;
    int count = 1;
    while (count < i and p != nullptr) {
        p = p->next;
        count++;
    }
    if (p == nullptr) {
        throw "查找位置错误";
    }
    else {
        return p->data;
        //std::cout << p->data << " ";
    }
}

template<typename DataType>
int LinkList<DataType>::Empty() {
    Node<DataType>* p = first->next;
    if (p != nullptr) {
        return 1;
    }
    else {
        return 0;
    }
}

template<typename DataType>
int LinkList<DataType>::Length() {
    Node<DataType>* p = first->next;
    int count = 0;
    if (p != nullptr) {
        p = p->next;
        count++;
    }
    return count;
}

template<typename DataType>
int LinkList<DataType>::Locate(DataType x)
{
    Node<DataType>* p = first->next; //工作指针p初始化
    int count = 1; //累加器count初始化
    while (p != nullptr)
    {
        if (p->data == x) return count; //查找成功，结束函数并返回序号
        p = p->next;
        count++;
    }
    return 0; //退出循环表明查找失败
}

template<typename DataType>
void LinkList<DataType>::Insert(int i, DataType x)
{
    Node<DataType>* p = first, * s = nullptr; //工作指针p初始化
    int count = 0;
    while (p != nullptr && count < i - 1) //查找第i – 1个结点
    {
        p = p->next; //工作指针p后移
        count++;
    }
    if (p == nullptr)
    {
        throw "插入位置错误";
    }
    else
    {
        s = new Node<DataType>; s->data = x; //申请结点s，数据域为x
        s->next = p->next; p->next = s; //将结点s插入到结点p之后
    }
}

/*
template<typename DataType>
const LinkList<DataType> difference(LinkList<DataType> a, LinkList<DataType> b) {
    LinkList<DataType> c;
    int length_a = a.Length();
    int length_b = b.Length();
    int count_a = 1;
    int count_c = 1;
    while (count_a <= length_a) {
        if (b.Locate(a.Get(count_a)) == 0) {
            c.Insert(count_c, a.Get(count_a));
            count_a++;
        }
        else {
            count_a++;
        }
    }
    return c;
}
*/

/*
template<typename DataType>
Node<DataType>* LinkList<DataType>::GetFirst()
{
    return first;
}
*/
template<typename DataType>
vector<DataType> difference(LinkList<DataType> a, LinkList<DataType> b)
{
    vector<DataType>v;
    //LinkList<DataType> c;
    Node<DataType>* p1 = a.first;
    Node<DataType>* p2 = b.first;
    p1 = p1->next;
    p2 = p2->next;
    int count = 0;
    while (true)
    {
        if (p1->data < p2->data)
        {
            v.push_back(p1->data);
            p1 = p1->next;
            count++;
        }
        else if (p1->data == p2->data)
        {
            p1 = p1->next;
            p2 = p2->next;
        }
        else if (p1->data > p2->data)
        {
            p2 = p2->next;
        }

        if (p1 == nullptr)
        {
            break;
        }

        if (p2 == nullptr and p1!=nullptr)
        {
            while (p1 != nullptr)
            {
                v.push_back(p1->data);
                //c.Insert(count, p1->data);
                count++;
                p1 = p1->next;
            }
            break;
        }
    }
    return v;
}


int main() {
    /*
    int array_a[4] = { 1, 2, 3, 4 };
    int array_b[5] = { 1, 2, 3, 4, 5 };
    int count_a = 4;
    int count_b = 5;
    int temp;
    for (int count = 0; count < count_a; count++) {
        std::cin >> temp;
        array_a[count] = temp;
    }
    for (int count = 0; count < count_b; count++) {
        std::cin >> temp;
        array_b[count] = temp;
    }
    */
    std::string str1;
    std::string str2;
    std::getline(cin, str1);
    std::getline(cin, str2);
    int array_a[100];
    int array_b[100];
    int i = 0;
    int j = 0;
    stringstream ss1(str1);
    while (ss1 >> array_a[i]) { i++; }
    stringstream ss2(str2);
    while (ss2 >> array_b[j]) { j++; }
    LinkList<int> a{ array_a, i };
    LinkList<int> b{ array_b, j };
    //a.PrintList();
    //b.PrintList();
    //vector<int> c;
    vector<int>c = difference(a, b);
    sort(c.begin(), c.end());
    for (int i = 0; i < c.size(); i++)
    {
        cout << c[i] << " ";
    }
    return 0;
}
