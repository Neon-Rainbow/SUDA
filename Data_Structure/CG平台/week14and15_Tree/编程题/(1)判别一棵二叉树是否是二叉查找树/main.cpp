#include <iostream>
#include <vector>

using namespace std;

struct Node
{
    int data;
    Node* left;
    Node* right;
};

class BinaryTree
{
public:
    BinaryTree();
    void InorderTreeWalk(Node* root);
    bool IsValidBST();
private:
    Node* _root;
    Node * Create();
    vector<int> v;
};

BinaryTree::BinaryTree()
{
    _root = Create();
}

Node * BinaryTree::Create()
{
    Node* root;
    int i;
    cin >> i;
    if(i == 0)
    {
        root = nullptr;
    }
    else
    {
        root = new Node;
        root->data = i;
        root->left = Create();
        root->right = Create();
    }
    return root;
}

void BinaryTree::InorderTreeWalk(Node *root)
{
    if(root != nullptr)
    {
        InorderTreeWalk(root->left);
        v.push_back(root->data);
        InorderTreeWalk(root->right);
    }
}

bool BinaryTree::IsValidBST()
{
    this->InorderTreeWalk(_root);
    int length = v.size();
    for(int i = 0; i < length - 1; i++)
    {
        if(v[i] > v[i+1])
        {
            return false;
        }
    }
    return true;
}


int main()
{
    BinaryTree(Tree){ };
    bool ans = Tree.IsValidBST();
    ans ? cout<<"True" : cout<<"False";
}
