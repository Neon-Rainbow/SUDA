#include "utility.h"
#include "BiTree.h"

template<typename DataType>
void Order(BiTree<DataType> tree)
{
    cout<<"判断二叉树是否为空"<<endl;
    if(tree.Empty() == 0){cout<<"二叉树为空"<<endl;}
    else
    {
        cout<<"二叉树不为空"<<endl;

        cout<<"进行先序遍历(递归)"<<endl;
        tree.RecursionPreOrder();
        cout<<""<<endl;
        cout<<"-------------------"<<endl;

        cout<<"进行先序遍历(非递归)"<<endl;
        tree.PreOrder();
        cout<<endl;
        cout<<"-------------------"<<endl;

        cout<<"进行中序遍历(递归)"<<endl;
        tree.RecursionInOrder();
        cout<<endl;
        cout<<"-------------------"<<endl;

        cout<<"进行中序遍历(非递归)"<<endl;
        tree.InOrder();
        cout<<endl;
        cout<<"-------------------"<<endl;

        cout<<"进行后序遍历(递归)"<<endl;
        tree.RecursionPostOrder();
        cout<<endl;
        cout<<"-------------------"<<endl;

        cout<<"进行层序遍历"<<endl;
        tree.LevelOrder();
        cout<<endl;
        cout<<"-------------------"<<endl;

        cout<<"二叉树的高度为:"<<tree.GetHeight()<<endl;
        cout<<"二叉树的节点数为:"<<tree.GetTreeSize(tree.GetRoot())<<endl;
        cout<<"二叉树的叶节点数为:"<<tree.GetLeafSize(tree.GetRoot())<<endl;

    }
}

void test()
{
    BiTree<char>T1{ };
    Order(T1);
    cout<<"------------------------"<<endl;
    cout<<"------------------------"<<endl;
    cout<<"进行拷贝构造"<<endl;
    const BiTree<char>&T2(T1);
    Order(T2);
}