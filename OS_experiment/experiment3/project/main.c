#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <unistd.h>
#include <time.h>

const int GAME_MSG_TYPE = 1;
const int QUEUE_PERMISSIONS = 0666;

typedef enum {
    SCISSORS = 0, // 剪刀
    ROCK = 1,     // 石头
    PAPER = 2     // 布
} RPS;

typedef enum {
    DRAW = 0, //平局
    PLAYER1_WINS = 1,
    PLAYER2_WINS = -1
} GameResult;


struct Game{
    long msgType; //消息类型,用于消息队列中识别消息
    int round; //表示玩家选择的手势（石头、剪刀、布）
};

// 向指定的消息队列发送游戏结果。
// 参数：
// - num: 消息将被发送到的消息队列标识符。
void result_send(const int num){
    struct Game game;
    game.msgType = GAME_MSG_TYPE; // 设置消息类型为1，用于消息队列
    game.round = rand() % 3; // 随机生成石头、剪刀、布
    printf("Sending message: Round %d, Type %ld\n", game.round, game.msgType);
    msgsnd(num, &game, sizeof(game) - sizeof(long), 0);
    printf("Message sent\n");
}

// 根据两位玩家的选择宣布一轮比赛的结果。
// 参数：
// - player1: 玩家1的选择。
// - player2: 玩家2的选择。
// 返回值：
// - 0 表示平局。
// - 1 如果玩家1赢。
// - -1 如果玩家2赢。
int result_announce(const int player1, const int player2){
    printf("Player 1: %d, Player 2: %d\n", player1, player2);
    if(player1 == player2){
        printf("Result: Draw\n");
        return DRAW; // 平局
    }else if((player1 - player2 + 3) % 3 == 1){
        printf("Result: Player 1 wins\n");
        return PLAYER1_WINS; // player1赢
    }else{
        printf("Result: Player 2 wins\n");
        return PLAYER2_WINS; // player2赢
    }
}

// 将所有轮次的结果写入文件并打印到控制台。
// 参数：
// - rounds: 总共进行的轮次数。
// - result_list: 包含每轮结果的数组。
void write_file(const int rounds, const int *result_list){
    int rounds_player1_win = 0;
    int rounds_player2_win = 0;
    int draw = 0;

    FILE *fin;
    if((fin = fopen("result.txt", "w")) == NULL){
        printf("文件没能打开\n");
        return;
    }

    for(int i = 0; i < rounds; i++){
        switch(result_list[i]){
            case 1:
                rounds_player1_win++;
                fprintf(fin, "NO.%d: A win\n", i + 1);
                printf("NO.%d: A win\n", i + 1);
                break;
            case -1:
                rounds_player2_win++;
                fprintf(fin, "NO.%d: B win\n", i + 1);
                printf("NO.%d: B win\n", i + 1);
                break;
            case 0:
                draw++;
                fprintf(fin, "NO.%d: draw\n", i + 1);
                printf("NO.%d: draw\n", i + 1);
                break;
        }
    }

    printf("最终结果: A获胜了%d局, B获胜了%d局, 平局了%d局\n",
           rounds_player1_win, rounds_player2_win, draw);
    fprintf(fin, "最终结果: A获胜了%d局, B获胜了%d局, 平局了%d局\n",
            rounds_player1_win, rounds_player2_win, draw);
    fclose(fin);
}

// 主函数，处理游戏的消息队列逻辑。
// 返回值：
// - 0 表示执行成功。
// - -1 表示失败。
int message_queue(){
    int rounds;
    printf("输入比赛的轮数: ");
    scanf("%d", &rounds);
    int *result_list = (int *)malloc(rounds * sizeof(int));
    if (result_list == NULL) {
        printf("内存分配失败\n");
        return -1;
    }

    int message_id1 = msgget(IPC_PRIVATE, IPC_CREAT | QUEUE_PERMISSIONS);
    int message_id2 = msgget(IPC_PRIVATE, IPC_CREAT | QUEUE_PERMISSIONS);

    if(message_id1 == -1 || message_id2 == -1){
        fprintf(stderr, "消息队列创建失败\n");
        free(result_list);
        return -1;
    }

    for(int i = 0; i < rounds; i++){
        pid_t pid1 = fork(), pid2;
        if(pid1 == 0){
            srand(time(NULL) ^ (getpid()<<16));
            printf("Player 1 process %d, Seed: %ld\n", getpid(), time(NULL) ^ (getpid()<<16));
            result_send(message_id1);
            exit(0);
        } else if (pid1 > 0) {
            pid2 = fork();
            if(pid2 == 0){
                srand(time(NULL) ^ (getpid()<<16));
                printf("Player 2 process %d, Seed: %ld\n", getpid(), time(NULL) ^ (getpid()<<16));
                result_send(message_id2);
                exit(0);
            }
        }

        if(pid1 < 0 || pid2 < 0){
            printf("fork失败\n");
        }else{
            wait(NULL); // 等待第一个子进程结束
            wait(NULL); // 等待第二个子进程结束

            struct Game game1, game2;
            // 从消息队列接收消息
            msgrcv(message_id1, &game1, sizeof(game1) - sizeof(long), 0, 0);
            msgrcv(message_id2, &game2, sizeof(game2) - sizeof(long), 0, 0);

            printf("Round %d, Player 1 chooses %d, Player 2 chooses %d\n", i+1, game1.round, game2.round);
            int result = result_announce(game1.round, game2.round);
            result_list[i] = result;
        }
    }

    write_file(rounds, result_list);

    // 清理
    msgctl(message_id1, IPC_RMID, NULL);
    msgctl(message_id2, IPC_RMID, NULL);
    free(result_list);

    return 0;
}

int main(){
    printf("Program started\n");
    srand(time(NULL)); // 仅在程序开始时设置一次随机种子
    message_queue();
    printf("Program finished\n");
    return 0;
}

