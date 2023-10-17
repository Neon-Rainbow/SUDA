#include<iostream>
#include <ctime>
#include <fstream>

using namespace std;

class Sort
{
public:
    Sort(int *a, int n);

    ~Sort() = default;

    void InsertionSort();

    void ShellSort();

    void SelectSort();

    void BubbleSort();

    void QuickSort(int first, int last);

    void HeapSort();

    void MergeSort(int p, int r);

    void MergeSort2();

    void Print();

private:
    //快速排序的划分
    int Partition(int first, int last);

    //构建最大堆和维护最大堆
    void MaxHeapify(int i);

    void BuildMaxHeap();

    int Left(int i)
    { return 2 * i + 1; }

    int Right(int i)
    { return 2 * i; }

    int Parent(int i)
    { return (i - 1) / 2; }

    //归并排序
    void Merge(int p, int q, int r);

    void MergePass(int h);

    int *data;
    int length;
    int count = 0;
};

Sort::Sort(int *a, int n)
{
    data = new int[n];
    for (int i = 0; i < n; i++)
    {
        this->data[i] = a[i];
    }
    this->length = n;
}

void Sort::InsertionSort()
{
    for (int j = 1; j < this->length - 1; j++)
    {
        int key = this->data[j];
        int i = j - 1;
        while (i >= 0 && this->data[i] > this->data[j])
        {
            this->data[i + 1] = this->data[i];
            i--;
        }
        this->data[i + 1] = key;
    }
}

void Sort::ShellSort()
{
    int d, i, j, temp;
    for (d = this->length / 2; d >= 1; d = d / 2)
    {
        for (i = d; i < length; i++)
        {
            temp = data[i];
            for (j = i - d; j >= 0 && temp < data[j]; j = j - d)
            {
                data[j + d] = data[j];
            }
            data[j + d] = temp;
        }
    }
}

void Sort::BubbleSort()
{
    int j, exchange, bound;
    exchange = length - 1;
    while (exchange != 0)
    {
        bound = exchange;
        exchange = 0;
        for (j = 0; j < bound; j++)
        {
            if (data[j] > data[j + 1])
            {
                swap(data[j], data[j + 1]);
                exchange = j;
            }

        }
    }
}

void Sort::QuickSort(int first, int last)
{
    if (first < last)
    {
        int p = Partition(first, last);
        QuickSort(first, p - 1);
        QuickSort(p + 1, last);
    }
}

int Sort::Partition(int first, int last)
{
    int p = data[first];
    int i = first;
    int j = last;
    while (i < j)
    {
        while (data[j] >= p && i < j)
        {
            j--;
        }
        while (data[i] <= p && i < j)
        {
            i++;
        }
        if (i < j)
        {
            swap(data[i], data[j]);
        }
    }
    swap(data[first], data[j]);
    return j;
}

void Sort::Print()
{
    for (int i = 0; i < length; i++)
    {
        cout << data[i] << " ";
    }
    cout << endl;
}

void Sort::HeapSort()
{
    int temp = length;
    for (int i = length - 1; i > -0; i--)
    {
        swap(data[0], data[i]);
        length--;
        MaxHeapify(0);
    }
    length = temp;
}

void Sort::MaxHeapify(int i)
{
    int l = Left(i);
    int r = Right(i);
    int largest;
    if (l < length && data[l] > data[i])
    {
        largest = l;
    } else
    {
        largest = i;
    }
    if (r < length && data[r] > data[largest])
    {
        largest = r;
    }
    if (largest != i)
    {
        swap(data[i], data[largest]);
        MaxHeapify(largest);
    }
}

void Sort::BuildMaxHeap()
{
    for (int i = length / 2 - 1; i >= 0; i--)
    {
        MaxHeapify(i);
    }
}

void Sort::MergeSort(int p, int r)
{
    if (p < r)
    {
        int q = (p + r) / 2;
        MergeSort(p, q);
        MergeSort(q + 1, r);
        Merge(p, q, r);
    } else
    {
        return;
    }
}

void Sort::Merge(int p, int q, int r)
{
    int temp[length];
    int i = p;
    int j = q + 1;
    int k = p;
    while (i <= q && j <= r)
    {
        if (data[i] <= data[j])
        {
            temp[k++] = data[i++];
        }
        else
        {
            temp[k++] = data[j++];
        }
    }
    while (i <= q)
    {
        temp[k++] = data[i++];
    }
    while (j <= r)
    {
        temp[k++] = data[j++];
    }
    for (i = p; i <= r; i++)
    {
        data[i] = temp[i];
    }
}

void Sort::MergePass(int h)
{
    int i = 0;
    while (i + 2 * h <= length)
    {
        Merge(i, i+h-1, i+2*h-1);
        i = i + 2 * h;
    }
    if (i + h < length)
        Merge(i, i+h-1, length-1);
}

void Sort::MergeSort2( )
{
    int h = 1;
    while (h < length)
    {
        MergePass(h);
        h = 2 * h;
    }
}

void Sort::SelectSort( )
{
    int i, j, index, temp;
    for (i = 0; i < length - 1; i++)
    {
        index = i;
        for (j = i + 1; j < length; j++)
            if (data[j] < data[index]) index = j;
        if (index != i) {
            temp = data[i]; data[i] = data[index]; data[index] = temp;
        }
    }
}

string fn(int type,int num)
{
    string filename;
    string type_filename;
    string num_filename;
    switch(type)
    {
        case 1:
            type_filename = "positive-order";
            break;
        case 2:
            type_filename = "negative-order";
            break;
        case 3:
            type_filename = "random-order";
            break;
        default:
            break;
    }
    switch(num)
    {
        case 1:
            num_filename = "1000.txt";
            break;
        case 2:
            num_filename = "3000.txt";
            break;
        case 3:
            num_filename = "10000.txt";
            break;
        default:
            break;
    }
    filename = R"(D:\Programming\C-CPP\Csteaching\experiment6-Sort\data)";
    return filename;
}

int GetNum(int num)
{
    switch (num)
    {
        case 1:
            return 1000;
        case 2:
            return 3000;
        case 3:
            return 10000;
        default:
            return -1;
    }
}


int main()
{
    cout<<"1.Insertion Sort\n2.Shell Sort\n3.Select Sort\n4.Bubble Sort\n5.Quick Sort\n6.Heap Sort\n7.Merge Sort\n";
    cout<<"选择一种排序方式\n";
    int select;
    cin>>select;

    cout<<"1.正序 2.逆序 3.随机\n";
    cout<<"选择数据的类型\n";
    int type;
    cin>>type;

    cout<<"1.1000 2.3000 3.10000\n";
    cout<<"选择数据的个数\n";
    int num;
    cin>>num;

    //auto filename = fn(type,num);
    string filename = R"(D:\Programming\C-CPP\Csteaching\experiment6-Sort\data\negative-order\10000.txt)";
    auto number = GetNum(num);
    auto begin = clock();
    const int length = number-1;

    int a[length];
    int temp;
    int count = 0;
    cout<<"文件名为:\t"<<filename<<endl;
    ifstream fin(filename);
    cout<<"数据个数为:\t"<<GetNum(num)<<endl;
    if(!fin.is_open())
    {
        cout<<"Open file wrong"<<endl;
        exit(0);
    }
    while(!fin.eof())
    {
        fin>>a[count];
        count++;
    }
    Sort(L)(a,length);
    switch(select)
    {
        case 1:
            cout<<"排序方式为:\tInsertionSort"<<endl;
            L.InsertionSort();
            break;
        case 2:
            cout<<"排序方式为:\tShellSort"<<endl;
            L.ShellSort();
            break;
        case 3:
            cout<<"排序方式为:\tSelectSort"<<endl;
            L.SelectSort();
            break;
        case 4:
            cout<<"排序方式为:\tBubbleSort"<<endl;
            L.BubbleSort();
            break;
        case 5:
            cout<<"排序方式为:\tQuickSort"<<endl;
            L.QuickSort(0,length-1);
            break;
        case 6:
            cout<<"排序方式为:\tHeapSort"<<endl;
            L.HeapSort();
            break;
        case 7:
            cout<<"排序方式为:\tMergeSort"<<endl;
            L.MergeSort(0,length-1);
            break;
        default:
            break;
    }
    //L.Print();
    auto end = clock();
    auto time  = end-begin;
    cout<<"运行时间为:\t"<<time<<endl;
}