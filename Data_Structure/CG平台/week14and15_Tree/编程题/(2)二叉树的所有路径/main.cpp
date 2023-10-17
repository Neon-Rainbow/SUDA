#include <iostream>
#include <vector>

//https://leetcode.cn/problems/binary-tree-paths/

using namespace std;

struct Node
{
    string val;
    Node* left;
    Node* right;
};

class BinaryTree
{
public:
    BinaryTree();
    void DFS()
    {DFS(_root, "");}
    vector<string> GetAns()
    {return ans;}
private:
    Node* _root;
    Node * Create();
    void DFS(Node* root, string path);
    vector<string> ans;
};

BinaryTree::BinaryTree()
{
    _root = Create();
}

Node * BinaryTree::Create()
{
    Node* root;
    string i;
    cin >> i;
    if(i == "#")
    {
        root = nullptr;
    }
    else
    {
        root = new Node;
        root->val = i;
        root->left = Create();
        root->right = Create();
    }
    return root;
}

void BinaryTree::DFS(Node *root, string path)
{
    if(root == nullptr)
    {
        return;
    }
    if(root->left == nullptr && root->right == nullptr)
    {
        path += root->val;
        ans.push_back(path);
        return;
    }
    path += (root->val + " ");
    DFS(root->left, path);
    DFS(root->right, path);
}

int main()
{
    BinaryTree(Tree){ };
    Tree.DFS();
    auto v = Tree.GetAns();
    for(const auto & i : v)
    {
        cout<<i<<endl;
    }
}