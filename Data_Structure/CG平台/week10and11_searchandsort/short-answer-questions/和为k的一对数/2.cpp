#include<iostream>
#include<vector>
using namespace std;

void TwoSum(vector<int> &v,int target)
{
    int i = 0;
    int j = v.size()-1;
    while(i<j)
    {
        if(v[i]+v[j]==target && i<j)
        {
            cout<<"第"<<i<<"号元素和第"<<j<<"号元素的和为target("<<target<<")";
            return;
        }
        else if(v[i]+v[j]<target && i<j)
        {
            i++;
        }
        else if(v[i]+v[j]>target && i<j)
        {
            j--;
        }
    }
    cout<<"v中找不到和为target("<<target<<")的两个数";
}

int main()
{
    vector<int>v{1,2,4,6,9};
    TwoSum(v,8);
}