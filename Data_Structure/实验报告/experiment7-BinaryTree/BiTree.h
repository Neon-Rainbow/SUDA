#include "utility.h"

template<typename DataType>
struct BiNode
{
    DataType data;
    BiNode<DataType>* left_child;
    BiNode<DataType>* right_child;
};

template<typename DataType>
struct element
{
    BiNode<DataType>* ptr;
    int flag;
};

template<typename DataType>
class BiTree
{
public:
    BiTree()
    {
        cout<<"请输入二叉树，#表示节点为空"<<endl;
        root  = Creat();
    }

    ~BiTree()
    {
        cout<<"Release"<<endl;
        Release(root);
    }

    BiTree(BiTree<DataType> const &T);

    BiNode<DataType>* GetRoot()
    {return this->root;}

    bool Empty()
    { return !(root == nullptr) ;}

    void RecursionPreOrder()
    {RecursionPreOrder(root);}

    void RecursionInOrder()
    {RecursionInOrder(root);}

    void RecursionPostOrder()
    {RecursionPostOrder(root);}

    void LevelOrder();

    void PreOrder()
    { PreOrder(root);}

    void InOrder()
    {InOrder(root);}

    void PostOrder()
    {PostOrder();}

    int GetHeight()
    {return GetHeight(root);}

    int GetTreeSize(BiNode<DataType>* node);

    int GetLeafSize(BiNode<DataType>* node);

    void Insert(BiNode<DataType>* insert_node);

private:
    BiNode<DataType> * Creat();

    void Release(BiNode<DataType>* bt);

    void RecursionPreOrder(BiNode<DataType>* bt);

    void RecursionInOrder(BiNode<DataType>* bt);

    void RecursionPostOrder(BiNode<DataType>* bt);

    BiNode<DataType>* root;

    void PreOrder(BiNode<DataType>* bt);

    void InOrder(BiNode<DataType>* bt);

    void PostOrder(BiNode<DataType>*bt);

    int GetHeight(BiNode<DataType>*bt);

    BiNode<DataType> * copy(BiNode<DataType>* node);
};

template<typename DataType>
BiNode<DataType> * BiTree<DataType>::Creat()
{
    BiNode<DataType>* bt;
    char ch;
    cin>>ch;
    if(ch =='#')
    {bt = nullptr;}
    else
    {
        bt = new BiNode<DataType>;
        bt->data = ch;
        bt->left_child = Creat();
        bt->right_child = Creat();
    }
    return bt;
}

template<typename DataType>
void BiTree<DataType>::Release(BiNode<DataType> *bt) //销毁二叉树采用后序遍历，其原因是为了防止将根节点销毁后找不到其左右子树。
{
    if(bt == nullptr)
    {return;}
    else
    {
        Release(bt->left_child);
        Release(bt->right_child);
        delete bt;
    }
}

template<typename DataType>
void BiTree<DataType>::RecursionPreOrder(BiNode<DataType> *bt)
{
    if(bt == nullptr)
    {return;}
    else
    {
        cout<<bt->data<<"\t";
        RecursionPreOrder(bt->left_child);
        RecursionPreOrder(bt->right_child);
    }
}

template<typename DataType>
void BiTree<DataType>::RecursionInOrder(BiNode<DataType> *bt)
{
    if(bt == nullptr)
    { return;}
    else
    {
        RecursionInOrder(bt->left_child);
        cout<<bt->data<<"\t";
        RecursionInOrder(bt->right_child);
    }
}

template<typename DataType>
void BiTree<DataType>::RecursionPostOrder(BiNode<DataType> *bt)
{
    if(bt == nullptr)
    { return;}
    else
    {
        RecursionPostOrder(bt->left_child);
        RecursionPostOrder(bt->right_child);
        cout<<bt->data<<"\t";
    }
}

template<typename DataType>
void BiTree<DataType>::LevelOrder()
{
    queue<BiNode<DataType>*>q;
    if(root!= nullptr)
    {
        q.push(root);
    }
    while (q.empty() == false)
    {
        auto temp = q.front();
        if(temp->left_child != nullptr)
        {
            q.push(temp->left_child);
        }
        if(temp->right_child != nullptr)
        {
            q.push(temp->right_child);
        }
        cout<<temp->data<<"\t";
        q.pop();
    }
}

template<typename DataType>
void BiTree<DataType>::PreOrder(BiNode<DataType> *bt)
{
    stack<BiNode<DataType>*> s;
    while(bt!= nullptr || s.empty()== false)
    {
        while(bt!= nullptr)
        {
            cout<<bt->data<<"\t";
            s.push(bt);
            bt = bt->left_child;
        }
        bt = s.top();
        s.pop();
        bt = bt->right_child;
    }
}

template<typename DataType>
void BiTree<DataType>::InOrder(BiNode<DataType> *bt)
{
    stack<BiNode<DataType>*> s;
    while(bt!= nullptr || s.empty()== false)
    {
        while(bt!= nullptr)
        {
            s.push(bt);
            bt = bt->left_child;
        }
        bt = s.top();
        cout<<bt->data<<"\t";
        s.pop();
        bt = bt->right_child;
    }
}

template<typename DataType>
void BiTree<DataType>::PostOrder(BiNode<DataType> *bt)
{
    element<DataType> S[100];                  //顺序栈，最多100个元素
    int top = -1;                       //顺序栈初始化
    while (bt != nullptr || top != -1)      //两个条件都不成立才退出循环
    {
        while (bt != nullptr)
        {
            top++;
            S[top].ptr = bt; S[top].flag = 1;      //bt连同标志flag入栈
            bt = bt->left_child;
        }
        while (top != -1 && S[top].flag == 2)
        {
            bt = S[top--].ptr;
            cout << bt->data;
        }
        if (top != -1) {
            S[top].flag = 2;
            bt = S[top].ptr->right_child;
        }
        else
            bt = nullptr;
    }
}

template<typename DataType>
int BiTree<DataType>::GetHeight(BiNode<DataType>*bt)
{
    int left_height;
    int right_height;
    if(bt== nullptr)
    {
        return 0;
    }
    else
    {
        left_height = GetHeight(bt->left_child);
        right_height = GetHeight(bt->right_child);
        return left_height>right_height?++left_height:++right_height;
    }
}

template<typename DataType>
int BiTree<DataType>::GetTreeSize(BiNode<DataType> *node)
{
    if(node == nullptr){return 0;}
    else
    {
        if(node->left_child == nullptr && node->right_child == nullptr)
        {
            return 1;
        }
    }
    return 1 + GetTreeSize(node->left_child) + GetTreeSize(node->right_child);
}

template<typename DataType>
int BiTree<DataType>::GetLeafSize(BiNode<DataType> *node)
{
    if(node == nullptr)
    {
        return 0;
    }
    else
    {
        if(node->left_child == NULL && node->right_child == NULL)
        {
            return 1;
        }
    }
    return GetLeafSize(node->left_child) + GetLeafSize(node->right_child);
}

template<typename DataType>
void BiTree<DataType>::Insert(BiNode<DataType> *insert_node)
{
    auto p = root;
    if(p == nullptr)
    {
        p = insert_node;
        p->left_child = nullptr;
        p->right_child = nullptr;
    }
    else
    {
        while(p!= nullptr)
        {
            p = p->left_child;
        }
        p = insert_node;
        p->left_child = nullptr;
        p->right_child = nullptr;
    }
}

template<typename DataType>
BiTree<DataType>::BiTree(BiTree<DataType> const &T)
{
    this->root = copy(T.root);
}

template<typename DataType>
BiNode<DataType> * BiTree<DataType>::copy(BiNode<DataType>* node)
{
    BiNode<DataType>* new_root;
    if(node == nullptr)
    {
        return nullptr;
    }
    else
    {
        auto left_node = copy(node->left_child);
        auto right_node = copy(node->right_child);
        new_root  = new BiNode<DataType>;
        new_root->left_child = left_node;
        new_root->right_child = right_node;
        new_root->data = node->data;
        return new_root;
    }
}