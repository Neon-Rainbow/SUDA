#include <iostream>
#include <ctime>
#include <fstream>
#include <random>

#define MaxSize 100000

class LineSearch
{
private:
    int data[MaxSize]{};
    int length;
public:
    LineSearch(const int a[], int n); //构造函数

    ~LineSearch() = default; //析构函数

    int SeqSearch(int data_to_be_searched); //线性查找

    int BinarySearch(int data_to_be_searched); //二分查找

    int RecursiveBinarySearch(int low, int high, int data_to_be_searched); //二分查找

    void Print(); //输出数组
};

LineSearch::LineSearch(const int a[], int n)
{
    //data = new int[n];
    for (int i = 0; i < n; i++)
    {
        this->data[i + 1] = a[i]; //data[0]设置为哨兵
    }
    this->length = n;
}

int LineSearch::SeqSearch(int data_to_be_searched)
{
    int i = this->length;
    this->data[0] = data_to_be_searched;
    while (data[i] != data_to_be_searched)
    {
        i--;
    }
    return i;
}

int LineSearch::BinarySearch(int data_to_be_searched)
{
    int mid;
    int low = 1;
    int high = this->length;
    while (low <= high)
    {
        mid = (low + high) / 2;
        if (data_to_be_searched < data[mid])
        {
            high = mid - 1;
        }
        else if (data_to_be_searched > data[mid])
        {
            low = mid + 1;
        }
        else
        {
            return mid;
        }
    }
    return 0;
}

int LineSearch::RecursiveBinarySearch(int low, int high, int data_to_be_searched)
{
    if (high < low)
    {
        return 0;
    }
    else
    {
        int mid = (low + high) / 2;
        int i = data[mid];
        if (data_to_be_searched < data[mid])
        { return RecursiveBinarySearch(low, mid - 1, data_to_be_searched); }
        else if (data_to_be_searched > data[mid])
        { return RecursiveBinarySearch(mid + 1, high, data_to_be_searched); }
        else
        { return mid; }
    }
}

void LineSearch::Print()
{
    for (int i = 0; i <= length; i++)
    {
        std::cout << data[i] << " ";
    }
    std::cout << std::endl;
}

LineSearch ReadFile(const std::string &filename) //读取文件并且返回一个LineSearch
{
    std::cout << "文件名为:\t" << filename << std::endl;
    std::cout << "数据个数为:\t50000" << std::endl;
    int length = 50000;
    int count = 0;
    int a[length];
    std::ifstream fin(filename);
    if (!fin.is_open())
    {
        std::cout << "Open file wrong" << std::endl;
        exit(0);
    }
    while (!fin.eof())
    {
        fin >> a[count];
        //std::cout<<a[count]<<" ";
        count++;
    }
    LineSearch(L){a, length};
    //L.Print();
    return L;
}

int RandomSearchNumber() //随机生成数字
{
    std::random_device rd;//用于生成随机数种子
    std::mt19937 r_eng(rd());//随机数生成器
    std::uniform_int_distribution<int> dis(1, 50000);//随机数分布器 闭区间
    //int i = dis(r_eng)*2+1;
    //return i;
    return dis(r_eng);
}

int Search(LineSearch L, int data_to_be_searched, int selected_search_method) //单次查找，查找的数为 data_to_be_searched
{
    int location_of_the_data_to_be_searched = -1;
    if (selected_search_method == 1)
    {
        location_of_the_data_to_be_searched = L.SeqSearch(data_to_be_searched);
    }
    else if (selected_search_method == 2)
    {
        location_of_the_data_to_be_searched = L.BinarySearch(data_to_be_searched);
    }
    else if (selected_search_method == 3)
    {
        location_of_the_data_to_be_searched = L.RecursiveBinarySearch(1, 50000, data_to_be_searched);
    }
    else
    {
        location_of_the_data_to_be_searched = 0;
    }
    return location_of_the_data_to_be_searched;
}

void WhetherToBeFound(int location_of_the_data_to_be_searched, int data_to_be_searched)
{
    if (location_of_the_data_to_be_searched == 0)
    {
        std::cout << "未找到" << data_to_be_searched << std::endl;
    }
    else
    {
        std::cout << "在第" << location_of_the_data_to_be_searched << "号位置查找到了" << data_to_be_searched
                  << std::endl;
    }
}

void TestMultipleSearch(LineSearch L, int select_search_method, int search_times)
{
    std::string output_filename = R"(D:\Programming\C-CPP\Csteaching\experiment5-Search\output\test_output_RecursiveBinarySearch.txt)";
    int success_times = 0;
    int fail_times = 0;
    std::fstream file_out(output_filename);
    file_out << "本次使用的查找方式为:\t二分查找(递归)\n";
    for (int i = 0; i < search_times; i++)
    {
        //int data_to_be_searched = RandomSearchNumber();
        int data_to_be_searched = i;
        int address = Search(L, data_to_be_searched, select_search_method);
        if (address == 0)
        {
            fail_times++;
            file_out << "本次查找的数据为:\t" << data_to_be_searched << std::endl;
            file_out << "查找结果为:\t失败" << std::endl;
        }
        else
        {
            success_times++;
            file_out << "本次查找的数据为:\t" << data_to_be_searched << std::endl;
            file_out << "查找结果为:\t成功" << std::endl;
        }
    }
    file_out << "查找次数:\n" << search_times << std::endl;
    file_out << "成功次数:\n" << success_times << std::endl;
    file_out << "失败次数:\n" << fail_times << std::endl;
    file_out.close();
    std::cout << "查找次数:\n" << search_times << std::endl;
    std::cout << "成功次数:\n" << success_times << std::endl;
    std::cout << "失败次数:\n" << fail_times << std::endl;
}

void MultipleSearch(LineSearch L, int select_search_method, int search_times) //多次查找，查找次数为search_times
{
    int success_times = 0;
    int fail_times = 0;
    for (int i = 0; i < search_times; i++)
    {
        int data_to_be_searched = RandomSearchNumber();
        //int data_to_be_searched = i;
        int address = Search(L, data_to_be_searched, select_search_method);
        if (address == 0)
        {
            fail_times++;
        }
        else
        {
            success_times++;
        }
    }
    std::cout << "查找次数:\n" << search_times << std::endl;
    std::cout << "成功次数:\n" << success_times << std::endl;
    std::cout << "失败次数:\n" << fail_times << std::endl;
}

int main()
{
    int select_search_method;
    int search_times;
    std::string filename = R"(D:\Programming\C-CPP\Csteaching\experiment5-Search\data\100000.txt)";
    auto L = ReadFile(filename);
    std::cout << "选择查找方式:\n1:顺序查找\n2:二分查找(非递归)\n3:二分查找(递归)" << std::endl;
    std::cin >> select_search_method;
    std::cout << "输入查找次数" << std::endl;
    std::cin >> search_times;
    auto begin = clock();
    MultipleSearch(L, select_search_method, search_times);
    auto end = clock();
    std::cout << "总运行时间:\t" << (double) (end - begin) << "ms" << std::endl;
    std::cout << "平均运行时间:\t" << (double) (end - begin) / search_times << "ms" << std::endl;
    return 0;
}
