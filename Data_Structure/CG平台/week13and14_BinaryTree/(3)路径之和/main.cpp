#include <iostream>
#include <queue>
#include <string>
#include <cstddef>

using namespace std;

struct Node
{
    string data;
    Node* left;
    Node* right;
};

class BinaryTree
{
public:
    BinaryTree();
    vector<vector<string>> LevelTreeWalk();
private:
    Node* _root;
    Node * Create();
    vector<vector<string>> LevelTreeWalk(Node* x);
};

BinaryTree::BinaryTree()
{
    _root = Create();
}

Node * BinaryTree::Create()
{
    Node* root;
    string ch;
    cin >> ch;
    if(ch == "#")
    {
        root = nullptr;
    }
    else
    {
        root = new Node;
        root->data = ch;
        root->left = Create();
        root->right = Create();
    }
    return root;
}

vector<vector<string>> BinaryTree::LevelTreeWalk()
{
    return LevelTreeWalk(_root);
}

vector<vector<string>> BinaryTree::LevelTreeWalk(Node* x)
{
    queue<Node *> q;
    vector<vector<string>> v;
    if (x != nullptr)
    { q.push(x); }
    while (!q.empty())
    {
        vector<string> every_level;
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

int main()
{
    BinaryTree(Tree){ };
    auto v = Tree.LevelTreeWalk();
    int sum = 0;
    for(size_t i = 0;i<v.size();i++)
    {
        for(size_t j = 0;j<v[i].size();j++)
        {
            sum+=i;
        }
    }
    cout<<sum<<endl;
}