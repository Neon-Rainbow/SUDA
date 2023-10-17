#include <iostream>

#define MaxSize 100

template<typename DataType>
struct Node {
    DataType data;
    Node<DataType> *next;
};

template<typename DataType>
class LinkList {
public:
    LinkList();

    LinkList(DataType a[], int n);

    void PairReverse();

    Node<DataType> *recursive_pair_reverse(Node<DataType> *L);

    void PrintList();

    void PrintListByNode(Node<DataType> *p);

    Node<DataType> *GetFirstNode() { return this->first; };

    int GetLength() { return this->length; }

private:
    Node<DataType> *first;
    int length;
};

template<typename DataType>
LinkList<DataType>::LinkList() {
    first = new Node<DataType>;
    first->next = nullptr;
    this->length = 0;

}

template<typename DataType>
LinkList<DataType>::LinkList(DataType a[], int n) {
    first = new Node<DataType>;
    this->length = n;
    Node<DataType> *p = first;
    first->data = a[0];
    Node<DataType> *s = nullptr;
    for (int i = 1; i < this->length; i++) {
        s = new Node<DataType>;
        s->data = a[i];
        p->next = s;
        p = p->next;
    }
    p->next = nullptr;
}

template<typename DataType>
void LinkList<DataType>::PairReverse() {
    Node<DataType> *p = first->next;
    Node<DataType> *q = p->next;

}

template<typename DataType>
Node<DataType> *LinkList<DataType>::recursive_pair_reverse(Node<DataType> *L) {
    if (L == nullptr || L->next == nullptr) { return L; }//递归边界条件
    else {
        Node<DataType> *p = L->next;
        Node<DataType> *q = p->next; //q为下一对需要逆置的节点的首节点
        p->next = L; //使第二个节点指向第一个节点,此时p成为了链表的第一个节点,L为链表的第二个节点
        L->next = recursive_pair_reverse(q);//递归
        return p;//返回链表的第一个节点,而非首节点
    }
}

template<typename DataType>
void LinkList<DataType>::PrintList() {
    Node<DataType> *p = first;
    while (p != nullptr) {
        std::cout << p->data << " ";
        p = p->next;
    }
    std::cout << std::endl;
}

template<typename DataType>
void LinkList<DataType>::PrintListByNode(Node<DataType> *p) {
    while (p != nullptr) {
        std::cout << p->data << " ";
        p = p->next;
    }
    std::cout << std::endl;
}


int main() {
    int n;
    int r[MaxSize];
    std::cin >> n;
    if (n == 0) {
        throw "输入的数组长度有误";
    } else {
        for (int i = 0; i < n; i++) {
            std::cin >> r[i];
        }
        LinkList<int> L{r, n};
        L.PrintListByNode(L.recursive_pair_reverse(L.GetFirstNode()));
    }
    return 0;
}
