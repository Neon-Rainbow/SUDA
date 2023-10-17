#include "utility.h"

struct BST_Node
{
    //Node->left->data < Node->data < Node->right->data
    int data;
    BST_Node *left;
    BST_Node *right;
    BST_Node *parent;
};

class BST
{
public:
    BST();

    BST(const vector<BST_Node *> &v);


    ~BST()
    {
        cout<<"Release"<<endl;
        Release(_root);
        exit(0);
    }

    BST_Node* GetRoot()
    {return _root;}

    void Insert(BST_Node *z);

    void PreorderTreeWalk()
    { PreorderTreeWalk(_root); }

    void InorderTreeWalk()
    { InorderTreeWalk(_root); }

    void PostTreeWalk()
    { PostorderTreeWalk(_root); }

    void LevelTreeWalk();

    void LevelTreeWalk2();

    BST_Node *Maximum()
    { return Maximum(_root); }

    BST_Node *Minimum()
    { return Minimum(_root); }

    BST_Node *TreeSearch(int k)
    { return TreeSearch(_root, k); }

    BST_Node *IterativeTreeSearch(int k)
    { return IterativeTreeSearch(_root, k); }

    BST_Node *TreeSuccessor(BST_Node *x);

    BST_Node *TreePredecessor(BST_Node *x);

    int GetTreeSize()
    { return GetTreeSize(_root); }

    int GetLeafSize()
    { return GetLeafSize(_root); }

    int GetHeight()
    { return GetHeight(_root); }

    void TreeDelete(BST_Node* z);

private:
    void Release(BST_Node* x);

    void PreorderTreeWalk(BST_Node *x);

    void InorderTreeWalk(BST_Node *x);

    void PostorderTreeWalk(BST_Node *x);

    vector<vector<int>> LevelTreeWalk2(BST_Node *x);

    BST_Node *Maximum(BST_Node *x);

    BST_Node *Minimum(BST_Node *x);

    BST_Node *TreeSearch(BST_Node *x, int k);

    BST_Node *IterativeTreeSearch(BST_Node *x, int k);

    int GetTreeSize(BST_Node *x);

    int GetLeafSize(BST_Node *x);

    int GetHeight(BST_Node *x);

    void Transplant(BST_Node *u, BST_Node *v); // 用一棵以v为根的子树替代一棵以u为根的子树

    BST_Node *_root{};
};

BST::BST()
{
    _root = nullptr;
}

BST::BST(const vector<BST_Node *> &v)
{
    for (auto i: v)
    {
        Insert(i);
    }
}

void BST::Insert(BST_Node *z)
{
    BST_Node *y = nullptr;
    BST_Node *x = this->_root;
    while (x != nullptr)
    {
        y = x;
        if (z->data < y->data)
        {
            x = x->left;
        }
        else
        {
            x = x->right;
        }
    }
    z->parent = y;
    if (y == nullptr)
    {
        this->_root = z; //empty tree
    }
    else if (z->data < y->data)
    {
        y->left = z;
    }
    else
    {
        y->right = z;
    }
    z->left = nullptr;
    z->right = nullptr;
}

void BST::PreorderTreeWalk(BST_Node *x)
{
    if (x != nullptr)
    {
        cout << x->data << "\t";
        PreorderTreeWalk(x->left);
        PreorderTreeWalk(x->right);
    }
}

void BST::InorderTreeWalk(BST_Node *x)
{
    if (x != nullptr)
    {
        InorderTreeWalk(x->left);
        cout << x->data << "\t";
        InorderTreeWalk(x->right);
    }
}

void BST::PostorderTreeWalk(BST_Node *x)
{
    if (x != nullptr)
    {
        PostorderTreeWalk(x->left);
        PostorderTreeWalk(x->right);
        cout << x->data << "\t";
    }
}

BST_Node *BST::Maximum(BST_Node *x)
{
    while (x->right != nullptr)
    {
        return Maximum(x->right);
    }
    return x;
}

BST_Node *BST::Minimum(BST_Node *x)
{
    while (x->left != nullptr)
    {
        return Minimum(x->left);
    }
    return x;
}

BST_Node *BST::TreeSearch(BST_Node *x, int k)
{
    if (x == nullptr or k == x->data)
    {
        return x;
    }
    if (k < x->data)
    {
        return TreeSearch(x->left, k);
    }
    else
    {
        return TreeSearch(x->right, k);
    }
}

BST_Node *BST::IterativeTreeSearch(BST_Node *x, int k)
{
    while (x != nullptr and k != x->data)
    {
        if (k < x->data)
        {
            x = x->right;
        }
        else
        {
            x = x->right;
        }
    }
    return x;
}

BST_Node *BST::TreeSuccessor(BST_Node *x)
{
    if (x->right != nullptr)
    {
        return Minimum(x->right);
    }
    auto y = x->parent;
    while (y != nullptr and x == y->right)
    {
        x = y;
        y = y->parent;
    }
    return y;
}

BST_Node *BST::TreePredecessor(BST_Node *x)
{
    if (x->left != nullptr)
    {
        return Maximum(x->left);
    }
    auto y = x->parent;
    while (y != nullptr and x == y->left)
    {
        x = y;
        y = y->parent;
    }
    return y;
}


int BST::GetTreeSize(BST_Node *x)
{
    if (x == nullptr)
    { return 0; }
    else if (x->left == nullptr and x->right == nullptr)
    {
        return 1;
    }
    return 1 + GetTreeSize(x->left) + GetTreeSize(x->right);
}

int BST::GetLeafSize(BST_Node *x)
{
    if (x == nullptr)
    {
        return 0;
    }
    else if (x->left == nullptr and x->right == nullptr)
    {
        return 1;
    }
    return GetLeafSize(x->left) + GetLeafSize(x->right);
}

int BST::GetHeight(BST_Node *x)
{
    int left_height;
    int right_height;
    if (x == nullptr)
    {
        return 0;
    }
    else
    {
        left_height = GetHeight(x->left);
        right_height = GetHeight(x->right);
        return left_height > right_height ? ++left_height : ++right_height;
    }
}

void BST::LevelTreeWalk()
{
    queue<BST_Node *> q;
    if (_root != nullptr)
    { q.push(_root); }
    while (!q.empty())
    {
        auto temp = q.front();
        q.pop();
        if (temp->left != nullptr)
        { q.push(temp->left); }
        if (temp->right != nullptr)
        { q.push(temp->right); }
        cout << temp->data << "\t";
    }
}

void BST::LevelTreeWalk2()
{
    vector<vector<int>> v = LevelTreeWalk2(_root);
    for(int count1 = 0;count1<v.size();count1++)
    {
        cout<<"第"<<count1+1<<"层:\t";
        for(int count2 : v[count1])
        {
            cout<<count2<<"\t";
        }
        cout<<endl;
    }
}


vector<vector<int>> BST::LevelTreeWalk2(BST_Node *x)
{
    queue<BST_Node *> q;
    vector<vector<int>> v;
    if (x != nullptr)
    { q.push(x); }
    while (!q.empty())
    {
        vector<int> every_level;
        int length_of_level = q.size();
        for (int i = 0; i < length_of_level; i++)
        {
            auto temp = q.front();
            q.pop();
            every_level.push_back(temp->data);
            if (temp->left != nullptr)
            { q.push(temp->left); }
            if (temp->right != nullptr)
            { q.push(temp->right); }
        }
        v.push_back(every_level);
    }
    return v;
}

void BST::Transplant(BST_Node *u, BST_Node *v) // 用一棵以v为根的子树替代一棵以u为根的子树
{
    if (u->parent == nullptr)
    {
        this->_root = v;  //u是树根
    }
    else if (u == u->parent->left)
    {
        u->parent->left = v;
    }
    else
    {
        u->parent->right = v;
    }
    if (v != nullptr)
    {
        v->parent = u->parent;
    }
}

void BST::TreeDelete(BST_Node *z)
{
    if(z->left == nullptr)
    {
        Transplant(z,z->right);
    }
    else if(z->right == nullptr)
    {
        Transplant(z,z->left);
    }
    else
    {
        auto y = TreeSuccessor(z);
        if(y->parent!=z)
        {
            Transplant(y,y->right);
            y->right = z->right;
            y->right->parent = y;
        }
        Transplant(z,y);
        y->left = z->left;
        y->left->parent = y;
    }
}

void BST::Release(BST_Node *x)
{
    if(x == nullptr)
    { return;}
    else
    {
        Release(x->left);
        Release(x->right);
        free(x);
    }
}



