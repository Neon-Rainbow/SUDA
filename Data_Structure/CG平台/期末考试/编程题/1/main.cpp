#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Node
{
    char val;
    Node *left;
    Node *right;
};

class BinaryTree
{
public:
    BinaryTree();

    void InorderTreeWalk(Node *root);

    void DeleteLeaf(Node *nd);

    Node *GetRoot() { return _root; }

private:
    Node *_root;

    Node *Create();
};

BinaryTree::BinaryTree() {
    _root = Create();
}

Node *BinaryTree::Create() {
    Node *root;
    char i;
    cin >> i;
    if (i == '#') {
        root = nullptr;
    } else {
        root = new Node;
        root->val = i;
        root->left = Create();
        root->right = Create();
    }
    return root;
}

void BinaryTree::InorderTreeWalk(Node *root) {
    if (root != nullptr) {
        InorderTreeWalk(root->left);
        cout << root->val;
        InorderTreeWalk(root->right);
    }
}

void BinaryTree::DeleteLeaf(Node *bt) {
    if (bt == nullptr) return;
    if (bt->left != nullptr) {
        if (bt->left->left == nullptr && bt->left->right == nullptr) {
            auto lbt = bt->left;
            bt->left = nullptr;
            delete lbt;
        } else DeleteLeaf(bt->left);
    }
    if (bt->right != nullptr) {
        if (bt->right->left == nullptr && bt->right->right == nullptr) {
            auto rbt = bt->right;
            bt->right = nullptr;
            delete rbt;
        } else DeleteLeaf(bt->right);
    }
}

int main() {
    BinaryTree(Tree){};
    Tree.DeleteLeaf(Tree.GetRoot());
    Tree.InorderTreeWalk(Tree.GetRoot());
}