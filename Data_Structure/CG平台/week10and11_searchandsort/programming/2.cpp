#include<iostream>
#define MaxSize 100

using namespace std;

int Partition(int *a,int p,int q)
{
    int x = a[p];
    int i = p;
    int j = q;
    while (i<j)
    {
        while(i<j && a[j]>= x)
        {
            j--;
        }
        while(i<j && a[i]<= x)
        {
            i++;
        }
        if(i<j)
        {
            swap(a[i],a[j]);
        }
    }
    swap(a[i],a[p]);
    return i;
}

void QuickSort(int a[],int p,int r)
{
    if(p<r)
    {
        int q = Partition(a,p,r);
        QuickSort(a,p,q-1);
        QuickSort(a,q+1,r);
    }
}

int Find(int *a,int p,int q,int k)
{
    int temp = Partition(a,p,q);
    if(temp == k-1)
    {
        return a[k-1];
    }
    else if(temp>k-1)
    {
        return Find(a,p,temp-1,k);
    }
    else
    {
        return Find(a,temp+1,q,k);
    }
}

int main()
{
    int n;
    int k;
    cin>>n>>k;
    int a[MaxSize];
    for(int i = 0;i<n;i++)
    {
        cin>>a[i];
    }
    /*
    QuickSort(a,0,9);
    for(int i = 0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
     */
    cout<<Find(a,0,n-1,k)<<endl;
}
