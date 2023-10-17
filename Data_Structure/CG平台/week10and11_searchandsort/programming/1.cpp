#include<iostream>

using namespace std;

struct Node
{
    int data;
    Node* next;
};

class LinkList
{
public:
    LinkList();
    LinkList(int a[], int n);
    void InsertSort();
private:
    Node* head;
};

LinkList::LinkList()
{
    head = new Node;
    head->next = nullptr;
}

LinkList::LinkList(int a[], int n)
{
    head = new Node;
    Node* r = head;
    Node* s = nullptr;
    for (int i = 0; i < n; i++)
    {
        s = new Node;
        s->data = a[i];
        r->next = s;
        r = s;
    }
    r->next = nullptr;
}

void LinkList::InsertSort()
{
    auto p = head->next;
    int a[20];
    int length = 0;
    while (p != nullptr)
    {
        a[length] = p->data;
        p = p->next;
        length++;
    }
    for (int j = 1; j < length; j++)
    {
        int key = a[j];
        int i = j - 1;
        while (i >= 0 && a[i] > key)
        {
            a[i + 1] = a[i];
            i--;
        }
        a[i + 1] = key;
    }
    for (int i = 0; i < length; i++)
    {
        cout << a[i] << " ";
    }
}

int main()
{
    int n;
    cin >> n;
    int a[20];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    LinkList(L) { a, n };
    L.InsertSort();
}