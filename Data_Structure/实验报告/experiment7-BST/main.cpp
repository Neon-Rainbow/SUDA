#include "utility.h"
#include "BST.h"


void Print(BST Tree)
{
    cout<<"中序遍历:"<<endl;
    Tree.InorderTreeWalk();
    cout<<endl;
    cout<<endl;

    cout<<"后续遍历:"<<endl;
    Tree.PostTreeWalk();
    cout<<endl;
    cout<<endl;

    cout<<"前序遍历:"<<endl;
    Tree.PreorderTreeWalk();
    cout<<endl;
    cout<<endl;

    cout<<"层序遍历:"<<endl;
    Tree.LevelTreeWalk2();
    cout<<endl;

    cout<<"BST的高度:"<<"\t"<<Tree.GetHeight()<<endl;
    cout<<"BST的节点数:"<<"\t"<<Tree.GetTreeSize()<<endl;
    cout<<"BST叶节点数:"<<"\t"<<Tree.GetLeafSize()<<endl;
    cout<<endl;

    cout<<"在BST中查找data为4的节点:"<<endl;
    if(Tree.TreeSearch(4)!= nullptr){cout<<"找到"<<endl;}
    else{cout<<"未找到"<<endl;}
    cout<<endl;

    cout<<"在BST中查找data为12的节点:"<<endl;
    if(Tree.TreeSearch(12)!= nullptr){cout<<"找到"<<endl;}
    else{cout<<"未找到"<<endl;}
    cout<<endl;

    cout<<"拷贝BST"<<endl;
    BST(Tree2){Tree};
    cout<<endl;

    cout<<"遍历拷贝之后的BST:"<<endl;
    Tree2.LevelTreeWalk2();
    cout<<endl;

    cout<<"在BST中删除data为6的节点"<<endl;
    Tree.TreeDelete(Tree.TreeSearch(6));
    cout<<endl;

    cout<<"删除后的BST:"<<endl;

    cout<<"中序遍历:"<<endl;
    Tree.InorderTreeWalk();
    cout<<endl;
    cout<<endl;

    cout<<"后续遍历:"<<endl;
    Tree.PostTreeWalk();
    cout<<endl;
    cout<<endl;

    cout<<"前序遍历:"<<endl;
    Tree.PreorderTreeWalk();
    cout<<endl;
    cout<<endl;

    cout<<"层序遍历:"<<endl;
    Tree.LevelTreeWalk2();
    cout<<endl;
}

int main()
{
    auto a = new BST_Node;
    auto b = new BST_Node;
    auto c = new BST_Node;
    auto d = new BST_Node;
    auto e = new BST_Node;
    auto f = new BST_Node;
    auto g = new BST_Node;
    auto h = new BST_Node;
    auto i = new BST_Node;
    auto j = new BST_Node;
    auto k = new BST_Node;
    a->data = 15;
    b->data = 6;
    c->data = 3;
    d->data = 2;
    e->data = 4;
    f->data = 7;
    g->data = 13;
    h->data = 9;
    i->data = 18;
    j->data = 17;
    k->data = 20;
    vector<BST_Node*>v{a,b,c,d,e,f,g,h,i,j,k};
    BST(Tree){v};
    Print(Tree);

    system("pause");
    return 0;
}