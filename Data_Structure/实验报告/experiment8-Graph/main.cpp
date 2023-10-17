#include <iostream>

using namespace std;

struct EdgeNode
{
    int adjvex;
    EdgeNode *next;
};

template<typename DataType>
struct VertexNode
{
    DataType vertex;
    EdgeNode *firstEdge;
};

const int MaxSize = 10;

template<typename DataType>
class MGraph
{
public:
    MGraph(DataType a[], int n, int e);

    void DFS();

    void DFS(int v, int visited[MaxSize]);

private:
    DataType vertex[MaxSize];
    int edge[MaxSize][MaxSize] = {0};
    int vertexNum, edgeNum;
};

template<typename DataType>
MGraph<DataType>::MGraph(DataType a[], int n, int e) {
    int i, j, k;
    vertexNum = n;
    edgeNum = e;
    cout << "请输入邻接点，例如:x y" << endl;
    for (i = 0; i < vertexNum; i++){
        vertex[i] = a[i];
    }
    for (k = 0; k < edgeNum; k++) {
        cin >> i >> j;
        edge[i][j] = 1;
        edge[j][i] = 1;
    }
}

template<typename DataType>
void MGraph<DataType>::DFS() {
    int visited[MaxSize] = {};
    for (int v = 0; v < vertexNum; v++)
        if (visited[v] == 0){
            DFS(v, visited);
        }
    cout << endl;
}

template<typename DataType>
void MGraph<DataType>::DFS(int v, int visited[MaxSize]) {
    cout << vertex[v] << " ";
    visited[v] = 1;
    for (int i = 0; i < vertexNum; i++){
        if (edge[v][i] == 1 && visited[i] == 0){
            DFS(i, visited);
        }

    }
}

template<typename DataType>
class ALGraph
{
public:
    ALGraph(DataType a[], int n, int e);

    ~ALGraph();

    void BFS();

private:
    VertexNode<DataType> adjlist[MaxSize];
    int vertexNum, edgeNum;
    int visited[MaxSize] = {0};
};

template<typename DataType>
ALGraph<DataType>::ALGraph(DataType a[], int n, int e) {
    int i, j, k;
    cout << "请输入邻接点，例如:x y" << endl;
    EdgeNode *s;
    vertexNum = n;
    edgeNum = e;
    for (i = 0; i < vertexNum; i++) {
        adjlist[i].vertex = a[i];
        adjlist[i].firstEdge = nullptr;
    }
    for (k = 0; k < edgeNum; k++) {
        cin >> i >> j;
        s = new EdgeNode;
        s->adjvex = j;
        s->next = adjlist[i].firstEdge;
        adjlist[i].firstEdge = s;
    }
}

template<typename DataType>
ALGraph<DataType>::~ALGraph() {
    EdgeNode *p, *q;
    for (int i = 0; i < vertexNum; i++) {
        p = q = adjlist[i].firstEdge;
        while (p != nullptr) {
            p = p->next;
            delete q;
            q = p;
        }
    }
}

template<typename DataType>
void ALGraph<DataType>::BFS() {
    int v = 0;
    int w, j, Q[MaxSize];
    int front = -1, rear = -1;
    EdgeNode *p = nullptr;
    cout << adjlist[v].vertex << " ";
    visited[v] = 1;
    Q[++rear] = v;
    while (front != rear) {
        w = Q[++front];
        p = adjlist[w].firstEdge;
        while (p != nullptr) {
            j = p->adjvex;
            if (visited[j] == 0) {
                cout << adjlist[j].vertex << " ";
                visited[j] = 1;
                Q[++rear] = j;
            }
            p = p->next;
        }
    }
    cout << endl;
}

int main() {
    char ch[] = {'A', 'B', 'C', 'D', 'E', 'F'};
    MGraph<char> MG(ch, 6, 7);
    cout << "邻接矩阵DFS:";
    MG.DFS();
    ALGraph<char> ALG(ch, 6, 7);
    cout << "邻接表BFS:";
    ALG.BFS();
    system("pause");
}
