package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	// 初始化缓冲读取器和写入器
	scanner := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	scanner.Split(bufio.ScanWords)

	// nextInt 是一个辅助函数，用于从输入中读取下一个整数
	nextInt := func() int {
		scanner.Scan()
		val, _ := strconv.Atoi(scanner.Text())
		return val
	}

	// 读取测试用例的数量
	t := nextInt()
	for ; t > 0; t-- {
		// 读取 n 的值
		n := nextInt()
		// 动态确定位集合的大小
		bitsetSize := (n + 64) / 64
		// 初始化位集合
		btst := make([]uint64, bitsetSize)

		// setBit 函数用于在 btst 中设置位
		setBit := func(pos int) {
			btst[pos/64] |= 1 << (pos % 64)
		}

		// getBit 函数用于获取 btst 中某一位的状态
		getBit := func(pos int) bool {
			return btst[pos/64]&(1<<(pos%64)) != 0
		}

		// 设置起始位
		setBit(0)

		// 主逻辑循环
		for i := 1; i <= n; i++ {
			x := nextInt()
			if i+x < n+1 {
				if getBit(i - 1) {
					setBit(i + x)
				}
			}
			if i-x-1 >= 0 {
				if getBit(i - x - 1) {
					setBit(i)
				}
			}
		}

		// 根据位集合的最终状态输出结果
		if getBit(n) {
			fmt.Fprintln(writer, "YES")
		} else {
			fmt.Fprintln(writer, "NO")
		}
	}
}
