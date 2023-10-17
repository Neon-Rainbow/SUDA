#include <pthread.h>
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <fstream>

#define MAT_SIZE 512 // 题目要求的矩阵行列数
#define NUM_THREADS 4 // 题目要求使用的线程数

std::vector<std::vector<int>> A(MAT_SIZE, std::vector<int>(MAT_SIZE));
std::vector<std::vector<int>> B(MAT_SIZE, std::vector<int>(MAT_SIZE));
std::vector<std::vector<int>> C(MAT_SIZE, std::vector<int>(MAT_SIZE));

struct thread_data {
    int start_row;
    int end_row;
};

void* multiply(void* arg) {
    auto data = static_cast<thread_data*>(arg);
    int start = data->start_row;
    int end = data->end_row;

    for (int i = start; i < end; i++) {
        for (int j = 0; j < MAT_SIZE; j++) {
            C[i][j] = 0;
            for (int k = 0; k < MAT_SIZE; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return nullptr;
}

void printMatrixToCSVFile(const std::vector<std::vector<int>>& matrix, const std::string& filename) {
    std::ofstream file(filename);

    if (!file) {
        std::cerr << "Unable to open the file " << filename << " for writing." << std::endl;
        return;
    }

    for (const auto& row : matrix) {
        for (size_t i = 0; i < row.size(); ++i) {
            file << row[i];
            if (i < row.size() - 1) {
                file << ',';
            }
        }
        file << '\n';
    }

    file.close();
    std::cout << "Matrix has been written to " << filename << std::endl;
}

int main() {
    pthread_t threads[NUM_THREADS];
    thread_data thread_data_array[NUM_THREADS];

    std::srand(std::time(nullptr));

    for (int i = 0; i < MAT_SIZE; i++) {
        for (int j = 0; j < MAT_SIZE; j++) {
            A[i][j] = std::rand() % 10;
            B[i][j] = std::rand() % 10;
        }
    }

    int rows_per_thread = MAT_SIZE / NUM_THREADS;

    for (int t = 0; t < NUM_THREADS; t++) {
        thread_data_array[t].start_row = t * rows_per_thread;
        thread_data_array[t].end_row = (t+1) * rows_per_thread;
        pthread_create(&threads[t], nullptr, multiply, &thread_data_array[t]);
    }

    for (auto & thread : threads) {
        pthread_join(thread, nullptr);
    }

    // 将矩阵 A, B 和 C 的值分别写入三个 CSV 文件
    printMatrixToCSVFile(A, "matrix_A.csv");
    printMatrixToCSVFile(B, "matrix_B.csv");
    printMatrixToCSVFile(C, "matrix_C.csv");

    return 0;
}
