#include<iostream>
#include<vector>


int sum1 = 0;
int sum2 = 0;
int CountingNumbers(int n)
{
	int mid = n / 2;
	if (n == 0) { return 1; }
	else if (n == 1) { return 1; }
	else
	{
		for (int i = 0; i <= mid; i++)
		{
			if (CountingNumbers(i) != 1)
			{
				;
			}
			else
			{
				sum2 += CountingNumbers(i);
			}
		}
		sum1 += sum2;
		sum2 = 0;
		return sum1;
	}	
}


int main()
{
	int n;
	std::cin >> n;
	std::cout << CountingNumbers(n);
	return 0;
}