#include <cstdio>
#include <cstdint>
#include <cstring>

// 计算给定数据块的CRC-16校验和
// crc: 初始CRC值
// mem: 指向数据块的指针
// len: 数据块的长度
uint16_t crc16k(uint16_t crc, uint8_t *mem, uint8_t len) {
    uint8_t *data = mem;

    // 如果数据块为空，则返回0
    if (data == nullptr) {
        return 0;
    }

    // 遍历数据块中的每个字节
    while (len--) {
        // 将当前字节与CRC值进行异或运算
        crc ^= *data++;
        // 对每个位进行处理
        for (uint8_t k = 0; k < 8; k++)
            // 如果当前位为1，则将CRC值右移一位并与多项式0x8408进行异或运算；否则，将CRC值右移一位
            crc = crc & 1 ? (crc >> 1) ^ 0x8408 : crc >> 1;
    }

    // 返回计算出的CRC-16校验和
    return crc;
}

int main() {
    char *str = "Hello World!";
    // 计算字符串"Hello World!"的CRC-16校验和，并将结果存储在checksum变量中
    uint16_t checksum = crc16k(0, (uint8_t *) str, strlen(str));
    // 打印校验和
    printf("Checksum: %04X\n", checksum);
}