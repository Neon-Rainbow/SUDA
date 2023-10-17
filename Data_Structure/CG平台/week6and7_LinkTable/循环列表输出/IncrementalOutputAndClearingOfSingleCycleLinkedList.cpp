#include <iostream>

using namespace std;

template<typename DataType>
struct Node {
    DataType data;
    Node<DataType> *next;
};

template<typename DataType>
class CirLinkList {
public:
    CirLinkList();

    CirLinkList(DataType a[], int n);

    void Insert(int i, DataType x);

    void PrintList();

    void PrintOrderedClear();

    void Delete(Node<DataType> *p); //删除p后面的节点
    ~CirLinkList() = default;

    int GetLength() { return this->length; };

    Node<DataType> *GetRearNode() { return this->rear; };
private:
    Node<DataType> *rear;
    int length;
};

template<typename DataType>
CirLinkList<DataType>::CirLinkList() {
    rear = new Node<DataType>;
    rear->next = rear;
}

template<typename DataType>
CirLinkList<DataType>::CirLinkList(DataType a[], int n) {
    rear = new Node<DataType>;
    rear->next = rear;
    Node<DataType> *p = rear->next; //p现在为循环单链表的第一个节点
    this->length = n;
    Node<DataType> *s = nullptr;
    for (int i = 0; i < n; i++) {
        s = new Node<DataType>;
        s->data = a[i];
        p->next = s;
        p = p->next;
    }
    p->next = rear;
}

template<typename DataType>
void CirLinkList<DataType>::Insert(int i, DataType x) {
    Node<DataType> *p = rear;
    Node<DataType> *s = nullptr;
    int count = 0;
    while (p->next != rear && count < i - 1) {
        p = p->next;
        count++;
    }
    s = new Node<DataType>;
    s->data = x;
    s->next = p->next;
    p->next = s;
    this->length++;
}

template<typename DataType>
void CirLinkList<DataType>::PrintList() {
    Node<DataType> *p = rear->next;
    while (p != rear) {
        cout << p->data << " ";
        p = p->next;
    }
    cout << endl;
}

template<typename DataType>
void CirLinkList<DataType>::PrintOrderedClear() {
    while (this->length != 0) {
        auto p = rear->next;
        auto p_prev = rear;
        auto min = rear->next;
        auto min_prev = rear;
        for (int i = 0; i < this->length; i++) {
            if (p->data < min->data) {
                min = p;
                min_prev = p_prev;
            }
            p = p->next;
            p_prev = p_prev->next;
        }
        cout << min->data << " ";
        this->Delete(min_prev);
    }
}

template<typename DataType>
void CirLinkList<DataType>::Delete(Node<DataType> *p) {
    Node<DataType> *p_next = p->next;
    p->next = p_next->next;
    this->length--;
    free(p_next);
}


int main() {

    int n, x;

    CirLinkList<int> L;

    cin >> n;

    for (int i = 1; i <= n; i++) {

        cin >> x;

        L.Insert(i, x);

    }

    L.PrintOrderedClear();

    return 0;

}
