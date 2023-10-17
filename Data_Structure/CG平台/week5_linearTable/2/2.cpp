#include <iostream>

#define MaxSize 20

template <class DataType>
class SeqList
{
public:
    SeqList(int a[], int n);
    void remove_k(int i, int k);
    void PrintList();
    void insert(DataType x);
private:
    DataType data[MaxSize];
    int length;
};

template <class DataType>
SeqList<DataType>::SeqList(int a[], int n)
{
    if (n > MaxSize)
    {
        throw "参数非法";
    }
    for (int i = 0;i < n;i++)
    {
        data[i] = a[i];
    }
    length = n;
}
template <class DataType>
void SeqList<DataType>::remove_k(int i, int k)
{
    if ((i <= 0) || ( i > 10) || (k==0)||(i + k > 11))
    {
        std::cout << "error"<<std::endl;
        exit(0);
    }
    else
    {
        for (int s = 0;s < k;s++)
        {
            for (int j = i;j < length;j++)
            {
                data[j - 1] = data[j];
            }
            length--;
        }
    }
}
template <class DataType>
void SeqList<DataType>::PrintList()
{
    for (int i = 0;i < length;i++)
    {
        std::cout << data[i]<<" ";
    }
    //std::cout<<std::endl;
}

template <class DataType>
void SeqList<DataType>::insert(DataType x)
{
    int k;
       if (x <= data[0])
	    {   
		    for (int i = length; i >= 1; i--)
		    {
		    	data[i] = data[i - 1];
		    }
		    data[0] = x;
		    length++;
	    }
	    else if (x >= data[length - 1])
	    {
		    data[length] = x;
		    length++;
	    }
        else 
        {
            for(int i = 0;i<length;i++)
            {
                if(x>=data[i] and x<= data[i+1])
                {
                    for(int j = length;j>=i+2;j--)
                    {
                        data[j] = data[j-1];
                    }
                    data[i+1] = x;
                    length++;
                    break;
                }
        }
        }
    
}
int main()
{
    int n = 10;
    int a;
    int r[10] = {1,3,5,7,9,11,13,15,17,19};
    SeqList<int>L{r,n};
    std::cin>>a;
    L.insert(a);
    L.PrintList();
    system("pause");
    return 0;
}