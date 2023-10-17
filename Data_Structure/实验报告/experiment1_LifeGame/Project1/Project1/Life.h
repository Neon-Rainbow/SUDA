#pragma once
#include<iostream>
#include<fstream>
#include<iomanip>
#include<iostream>
#include <string>
using namespace std;

const int maxrow = 20, maxcol = 60; //living cells共有20行，60列

class Life
{ //存放在*.h文件中的类体声明
public:
	void initialize(); //初始化living cells的状态
	void print(); //打印输出当前living cells的状态
	void update(); //进行deadliving间的转换
private:
	int grid[maxrow + 2][maxcol + 2]; //借助两维数组存放living cells
	//注意：为处理一致，添加了虚拟的2行2列，放围墙
	int neighbor_count(int row, int col); //统计邻居cell的状态
};
void Life::initialize()
{
	int choice;
	cout << "\nHow would you like to enter the data? \nChoose 1 if you want to directly input data,\nChoose 2 if you want to import coordinate data from a file.\nChoose 3 if you want to import the entire table directly from a file:" << endl;
	cin >> choice;
	if (choice == 1)
	{
		int row, col;
		for (row = 0; row <= maxrow + 1; row++)
			for (col = 0; col <= maxcol + 1; col++)
				grid[row][col] = 0;
		cout << "List the coordinates for living cells" << endl;
		cout << "Terminate the list with the special pair(-1, -1)" << endl;
		cin >> row >> col;
		while (row != -1 || col != -1)
		{
			if (row >= 1 && row <= maxrow)
				if (col >= 1 && col <= maxcol) grid[row][col] = 1;
				else cout << "Column" << col << " is out of range" << endl;
			else cout << "Row" << row << " is out of range" << endl;
			cin >> row >> col;
		}
	}
	else if (choice == 2 or choice == 3)
	{
		string address;
		cout << "Please enter the address of the file:" << endl;
		cin >> address; //输入文件的地址
		ifstream fin(address); //导入文件
		if (choice == 2)
		{
			int row, col;
			for (row = 0; row <= maxrow + 1; row++)
				for (col = 0; col <= maxcol + 1; col++)
					grid[row][col] = 0;
			fin >> row >> col;
			while (row != -1 || col != -1)
			{
				if (row >= 1 && row <= maxrow)
					if (col >= 1 && col <= maxcol) grid[row][col] = 1;
					else cout << "Column" << col << " is out of range" << endl;
				else cout << "Row" << row << " is out of range" << endl;
				fin >> row >> col;
			}
		}
		else if (choice == 3)
		{
			string temp;
			int r = -1;
			char temp_matrix[maxrow + 2][maxcol + 2];
			while (fin.eof() == false)
			{
				getline(fin, temp);
				r++;
				for (int i = 0; i < temp.size(); i++)
				{
					temp_matrix[r + 1][i + 1] = temp[i];
				}
			}
			for (int i = 0; i < maxrow; i++)
			{
				for (int j = 0; j < maxcol; j++)
				{
					if (temp_matrix[i][j] == '*')
					{
						grid[i][j] = 1;
					}
				}
			}
		}
	}
}


void Life::print()
{
	int row, col;
	cout << "\nThe current Life configuration is : " << endl;
	for (row = 1; row <= maxrow; row++)
	{
		for (col = 1; col <= maxcol; col++)
			if (grid[row][col] == 1) cout << " * ";
			else cout << " ";
		cout << endl;
	}
	cout << endl;
}

void Life::update()
{
	int row, col, new_grid[maxrow + 2][maxcol + 2];
	for (row = 1; row <= maxrow; row++)
		for (col = 1; col <= maxcol; col++)
			switch (neighbor_count(row, col))
			{
				//调用统计函数,按结果分情况
			case 2: new_grid[row][col] = grid[row][col]; break;//不变
			case 3: new_grid[row][col] = 1; break; //激活
			default: new_grid[row][col] = 0; //dead
			}
	for (row = 1; row <= maxrow; row++)
		for (col = 1; col <= maxcol; col++)
			grid[row][col] = new_grid[row][col];//将临时数组中的数据拷贝回原grid数组
}

int Life::neighbor_count(int row, int col)
{
	int i, j, count = 0;
	for (i = row - 1; i <= row + 1; i++)
		for (j = col - 1; j <= col + 1; j++)
			count += grid[i][j];//如果存活，则累加；否则为0
	count -= grid[row][col]; //去除自己
	return count;
}