#include <iostream>
#include <vector>

using namespace std;

template<typename DataType>
struct Node
{
    DataType data;
    Node* next;
};

template<typename DataType>
class LinkList
{
public:
    LinkList();
    LinkList(vector<DataType>v);
    void PrintList();
    Node<DataType>* GetMid(Node<DataType>* head);
    void MergeSort();
private:
    Node<DataType>* head;
    Node<DataType>* MergeSort(Node<DataType>* head);
};

template<typename DataType>
LinkList<DataType>::LinkList()
{
    head = new Node<DataType>;
    head->next = nullptr;
}

template<typename DataType>
LinkList<DataType>::LinkList(vector<DataType> v)
{
    head = new Node<DataType>;
    Node<DataType>* p = head;
    head->data = v[0];
    Node<DataType>* s = nullptr;
    for(int i = 1;i<v.size();i++)
    {
        s = new Node<DataType>;
        s->data = v[i];
        p->next = s;
        p = p->next;
    }
    p->next = nullptr;
}

template<typename DataType>
void LinkList<DataType>::PrintList()
{
    auto p = head;
    while(p!= nullptr)
    {
        cout<<p->data<<" ";
        p = p->next;
    }
    cout<<endl;
}

template<typename DataType>
Node<DataType> *LinkList<DataType>::GetMid(Node<DataType> *head)
{
    auto fast = head;
    auto slow = head;
    while(fast->next!= nullptr && fast->next->next != nullptr)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    return slow;

}

template<typename DataType>
Node<DataType> *LinkList<DataType>::MergeSort(Node<DataType> *head)
{
    if(head == nullptr || head->next== nullptr)
    {
        return head;
    }
    Node<DataType>* mid = GetMid(head);
    auto second = mid->next;
    mid->next = nullptr;
    auto left_list = MergeSort(head);
    auto right_list = MergeSort(second);
    return Merge(left_list,right_list);
}

template<typename DataType>
void LinkList<DataType>::MergeSort()
{
    head = MergeSort(head);
}


template<typename DataType>
Node<DataType> *Merge(Node<DataType> *list1, Node<DataType> *list2)
{
    if(list1 == nullptr)
    {return list2;}
    else if(list2 == nullptr)
    {return list1;}
    else if(list1->data<list2->data)
    {
        list1->next = Merge(list1->next,list2);
        return list1;
    }
    else
    {
        list2->next = Merge(list1,list2->next);
        return list2;
    }
}

template<typename DataType>
void Print(Node<DataType>* head)
{
    while(head!= nullptr)
    {
        cout<<head->data<<" ";
        head = head->next;
    }
    cout<<endl;
}

int main()
{
    vector<int> v2 {1,4,3,2,8,7,6,5,9,8};
    LinkList<int> L2{v2};
    cout<<"排序前的链表:";
    L2.PrintList();
    cout<<"排序后的链表:";
    L2.MergeSort();
    L2.PrintList();
    cout<<endl;
    vector<int> v3 {5,4,3,2,1,0};
    LinkList<int> L3{v3};
    cout<<"排序前的链表:";
    L3.PrintList();
    cout<<"排序后的链表:";
    L3.MergeSort();
    L3.PrintList();


    return 0;
}
