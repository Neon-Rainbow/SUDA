/*
A和B两个同学玩简单的纸牌游戏，每人手里有n张牌，两人轮流出牌并依次排列在桌面上，每次出掉手里的第1张牌，出牌后如果发现桌面上有跟刚才打出的牌的数字相同，
则把到相同的那张牌结束的全部牌按次序放在自己手里牌的末尾。当一人手中牌先出完时，游戏结束，对方获胜。
如n为5，A手里的牌依次为2 3 5 6 ，B手里的牌依次为1 5 4 2 ，
A出2，B出1；此时，桌子上从前往后依次为21，A手里是356，B手里是542；
A出3，B出5；此时，桌子上从前往后依次为2135，A手里是56，B手里是42；
接着A出5，发现前面有一张5，则把两个5都拿掉，这时他手里有6 5 5；桌子上的牌依次为2 1 3；接着B出4，桌子上的牌是2134，他手里的牌是2；
接着A出6， A手里剩55，B出2，发现前面有2，全部收走到自己手里，它手上的牌即是：264312桌子上没有牌；依次类推，直到某人先出完牌为止，则对方是胜者。
*/
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
using namespace std;


void PlayerPile(queue<int>&pile_in_player, vector<int>&pile_on_table) //PlayerPile函数用来控制每一次A和B打出的牌
{
    int temp_card = pile_in_player.front(); //取出玩家手中的第一张牌
    pile_in_player.pop();
    int card_position = -1;//card_position用来表示玩家手中的第一张牌在牌堆中的位置。若玩家手中的第一张牌不在牌堆中，则card_position为-1。在牌堆中则返回在牌堆中的位置
    for (int i = 0; i < pile_on_table.size(); i++) //判断玩家手中的第一张牌在牌堆中的位置
    {
        if (pile_on_table[i] == temp_card)
        {
            card_position = i;
            break;
        }
    }

    if (card_position != -1)//玩家打出的牌在牌堆中有一样的牌
    {
        pile_on_table.push_back(temp_card);//将玩家手中的牌放入牌堆中
        for (int i = pile_on_table.size()-1; i >= card_position; i--) //将牌堆中把直到相同牌的所有牌逆序放置在玩家手中
        {
            pile_in_player.push(pile_on_table[i]);
        }
        pile_on_table.erase(pile_on_table.begin() + card_position, pile_on_table.end());
    }
    else if(card_position == -1)//玩家打出的牌在牌堆中没有一样的牌
    {
        pile_on_table.push_back(temp_card);
    }
}

const string whoWin(queue<int>pile_A, queue<int>pile_B)//用来判断是否有玩家获胜。若有玩家获胜，则返回玩家的名字。若没有玩家获胜则返回None
{
    if (pile_A.size() == 0) { return "B"; }
    else if (pile_B.size() == 0) { return "A"; }
    else { return "None"; }
}

void printPile(queue<int>pile_A, queue<int>pile_B, vector<int>pile_table) //输出两名玩家手中的牌以及牌堆中的牌
{
    cout << "the cards on the desk:";
    for (int i = 0; i < pile_table.size(); i++)
    {
        cout << pile_table[i] << " ";
    }
    cout << endl;
    cout << "the cards in A:" << " ";
    int pile_A_size = pile_A.size();
    for (int i = 0; i < pile_A_size; i++)
    {
        cout << pile_A.front() << " ";
        pile_A.push(pile_A.front());
        pile_A.pop();
    }
    cout << endl;
    cout << "the cards in B:" << " ";
    int pile_B_size = pile_B.size();
    for (int i = 0; i < pile_B_size; i++)
    {
        cout << pile_B.front() << " ";
        pile_B.push(pile_B.front());
        pile_B.pop();
    }
    cout << endl;
    cout << "************************************************" << endl;
}
void PrintPileOfWinner(string winner,queue<int>pile_winner) //有玩家获胜时输出获胜玩家手中的牌
{
    cout << "胜者为" << winner << "," << winner << "剩下的牌为" << " ";
    int pile_winner_size = pile_winner.size();
    for (int i = 0; i < pile_winner_size; i++)
    {
        cout << pile_winner.front() << " ";
        pile_winner.push(pile_winner.front());
        pile_winner.pop();
    }
}

int main()
{
    queue<int>pile_A; //玩家A手中的牌
    queue<int>pile_B; //玩家B手中的牌

    cout << "请输入A手中的牌,每张牌之间用空格隔开，输入完后请输入0" << endl;
    while (true)
    {
        int a;
        cin >> a;
        if (a != 0)
        {
            pile_A.push(a);
        }
        else
        {
            break;
        }
    }
    cout << "请输入B手中的牌,每张牌之间用空格隔开，输入完后请输入0" << endl;
    while (true)
    {
        int a;
        cin >> a;
        if (a != 0)
        {
            pile_B.push(a);
        }
        else
        {
            break;
        }
    }
    cout << "输入完成" << endl;
    cout << "--------------------------------------" << endl;;
    //test
    //pile_A.push(2); pile_A.push(3); pile_A.push(5); pile_A.push(6);
    //pile_B.push(1); pile_B.push(5); pile_B.push(4); pile_B.push(2);
    vector<int>pile_table; //牌堆中的牌
    while (true)
    {
        if (whoWin(pile_A, pile_B) == "None")
        {
            printPile(pile_A, pile_B, pile_table);
            PlayerPile(pile_A,pile_table); //A出牌
            if (whoWin(pile_A, pile_B) == "None")
            {
                PlayerPile(pile_B, pile_table);//B出牌
                if (whoWin(pile_A, pile_B)=="None")
                {
                    ;
                }
                else
                {
                    goto Label;
                }
            }
            else
            {
                goto Label;
            }
        }
        else
        {
            goto Label;
        }
    
    }
Label: //一旦有人获胜则跳出while循环
    printPile(pile_A, pile_B,pile_table);
    string winner = whoWin(pile_A, pile_B);
    if (winner == "A")
    {
        PrintPileOfWinner("A", pile_A);
    }
    else if (winner == "B")
    {
        PrintPileOfWinner("B", pile_B);
    }
    cout << endl;
    system("pause");
    return 0;
}