#include <iostream>
#include <utility>
#include <vector>
#include <string>
#include <stack>

using namespace std;

class BinaryTree
{
public:
    BinaryTree() = default;

    explicit BinaryTree(vector<char> v);

    void Print();

    void PreorderTreeWalk() { PreorderTreeWalk(_vec); }

    void PreorderTreeWalk2() { PreorderTreeWalk2(0); }

private:
    vector<char> _vec;

    int Left(int i) { return 2 * i + 1; }

    int Right(int i) { return 2 * i + 2; }

    int Parent(int i) { return (i - 1) / 2; }

    void PreorderTreeWalk(vector<char> v);

    void PreorderTreeWalk2(int index);
};

BinaryTree::BinaryTree(vector<char> v) {
    _vec = std::move(v);
}

void BinaryTree::Print() {
    for (auto i: _vec) {
        cout << i << "|";
    }
}

void BinaryTree::PreorderTreeWalk(vector<char> v) {
    stack<int> st;
    int index = 0;
    int length = v.size();
    while (index < length || !st.empty()) {
        while (index < length) {
            if (v[index] != ' ') {
                cout << v[index];
            }
            st.push(index);
            index = Left(index);
        }
        if (!st.empty()) {
            index = st.top();
            st.pop();
            index = Right(index);
        }
    }
}

void BinaryTree::PreorderTreeWalk2(int index) {
    if (index < _vec.size()) {
        if (_vec[index] != ' ') {
            cout << _vec[index];
        }
        PreorderTreeWalk2(Left(index));
        PreorderTreeWalk2(Right(index));
    }
}


int main() {
    string a;
    getline(cin, a);
    vector<char> v;
    for (const char &i: a) {
        v.push_back(i);
    }
    BinaryTree(Tree){v};
    //Tree.Print();
    Tree.PreorderTreeWalk2();
}
