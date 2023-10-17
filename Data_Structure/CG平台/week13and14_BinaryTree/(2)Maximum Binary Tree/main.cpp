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
    BinaryTree(vector<int> v);
    void PreorderTreeWalk();
private:
    Node* _root;
    Node *Create(const vector<int>& nums);
    void PreorderTreeWalk(Node* root);
};

BinaryTree::BinaryTree(vector<int> v)
{
    _root = Create(v);
}

Node * BinaryTree::Create(const vector<int>& nums)
{
    int index = 0;
    if(nums.empty())
    {
        return nullptr;
    }
    else
    {
        for(int i = 0; i < nums.size(); i++)
        {
            if(nums[i] > nums[index])
            {
                index = i;
            }
        }
        auto root = new Node;
        root->data = nums[index];
        root->left = Create(vector<int>{nums.begin(), nums.begin()+index});
        root->right = Create(vector<int>{nums.begin()+index+1,nums.end()});
        return root;
    }
}

void BinaryTree::PreorderTreeWalk()
{
    PreorderTreeWalk(_root);
}

void BinaryTree::PreorderTreeWalk(Node *root)
{
    if(root!= nullptr)
    {
        cout<<root->data<<" ";
        PreorderTreeWalk(root->left);
        PreorderTreeWalk(root->right);
    }
}

int main()
{
    int length;
    cin>>length;
    vector<int>v;
    for(int i = 0;i < length; i++)
    {
        int temp = 0;
        cin>>temp;
        v.push_back(temp);
    }
    BinaryTree(Tree){v};
    Tree.PreorderTreeWalk();
}