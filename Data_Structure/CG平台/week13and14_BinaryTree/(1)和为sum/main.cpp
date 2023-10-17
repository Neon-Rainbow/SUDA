#include <iostream>

using namespace std;

struct TreeNode
{
    int val;
    TreeNode* left;
    TreeNode* right;
};

class BinaryTree
{
public:
    BinaryTree();
    void PathSum(int sum);
    int ans = 0;
private:
    TreeNode* _root;
    TreeNode * Create();
    void DFS(TreeNode* root, int sum);
};

BinaryTree::BinaryTree()
{
    _root = Create();
}

TreeNode * BinaryTree::Create()
{
    TreeNode* root;
    int i;
    cin >> i;
    if(i == 0)
    {
        root = nullptr;
    }
    else
    {
        root = new TreeNode;
        root->val = i;
        root->left = Create();
        root->right = Create();
    }
    return root;
}

void BinaryTree::PathSum(int sum)
{
    if(_root != nullptr)
    {
        DFS(_root, sum);
    }
    ans ? cout<<1<<endl : cout<<0<<endl;
}



void BinaryTree::DFS(TreeNode *root, int sum)
{
    if(root == nullptr)
    {
        return;
    }
    if(root->val == sum)
    {
        ans++;
    }
    DFS(root->left, sum-root->val);
    DFS(root->right, sum-root->val);
}

int main()
{
    BinaryTree(Tree){ };
    int sum;
    cin>>sum;
    Tree.PathSum(sum);
}
