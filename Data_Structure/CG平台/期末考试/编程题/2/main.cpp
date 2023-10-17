// Project3.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>

using namespace std;

template<class DataType>
struct BiNode
{
    DataType data;
    BiNode<DataType> *lchild, *rchild;
    int count;//增加的域
    BiNode(DataType val) {
        this->data = val;
        this->count = 0;
    }
};

template<class DataType>
class BiTree
{
public:
    BiTree() {
        root = nullptr;
    }

    void creat() {
        root = rec_creat();
    }

    ~BiTree() {
        rec_release(root);
    }

    void inorder() {
        rec_inorder(root);  //  中序遍历二叉树接口方法，用于输出每个结点的count值
    }

    void set_count();    //  接口方法,为二叉树的每个结点置count值

protected:
    BiNode<DataType> *rec_creat();

    void rec_release(BiNode<DataType> *&sub_root);

    void rec_inorder(BiNode<DataType> *sub_root);

    void rec_set_count(BiNode<DataType> *sub_root);    //需要完成的递归函数

    int change(BiNode<DataType> *nd, int cnt);

    BiNode<DataType> *root;
};

template<class DataType>
BiNode<DataType> *BiTree<DataType>::rec_creat() {
    char ch;
    cin >> ch;
    BiNode<DataType> *bt;
    if (ch == '#') bt = nullptr;
    else {
        bt = new BiNode<DataType>(ch);
        bt->lchild = rec_creat();
        bt->rchild = rec_creat();
    }
    return bt;
}

template<class DataType>
void BiTree<DataType>::rec_release(BiNode<DataType> *&sub_root) {
    if (sub_root == nullptr) return;
    else {
        rec_release(sub_root->lchild);
        rec_release(sub_root->rchild);
        delete sub_root;
        sub_root = nullptr;
    }
}

template<class DataType>
void BiTree<DataType>::rec_inorder(BiNode<DataType> *sub_root) {
    if (sub_root == nullptr) return;
    else {
        rec_inorder(sub_root->lchild);
        cout << sub_root->count;
        rec_inorder(sub_root->rchild);
    }
}

template<class DataType>
void BiTree<DataType>::set_count() {
    rec_set_count(root);  //  接口方法,为二叉树的每个结点置count值
}

template<class DataType>
int BiTree<DataType>::change(BiNode<DataType> *nd, int cnt) {
    if (nd == nullptr) return cnt;
    cnt++;
    cnt = change(nd->lchild, cnt);
    cnt = change(nd->rchild, cnt); //对左右子树递归
    return cnt;
}

template<class DataType>
void BiTree<DataType>::rec_set_count(BiNode<DataType> *sub_root) {
    //需要完成的递归函数
    if (sub_root == nullptr){
        return;
    }
    sub_root->count = change(sub_root->rchild, 0);
    rec_set_count(sub_root->lchild);
    rec_set_count(sub_root->rchild);
}

int main() {
    BiTree<char> bt;
    bt.creat();
    bt.set_count();
    bt.inorder();
    return 0;
}


