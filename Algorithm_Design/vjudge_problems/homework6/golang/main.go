package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const MaxLength = 200001

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	scanner.Split(bufio.ScanWords)

	nextInt := func() int {
		scanner.Scan()
		val, _ := strconv.Atoi(scanner.Text())
		return val
	}

	t := nextInt()
	for ; t > 0; t-- {
		n := nextInt()
		btst := make([]bool, MaxLength)
		btst[0] = true

		for i := 1; i <= n; i++ {
			x := nextInt()
			if i+x < MaxLength {
				btst[i+x] = btst[i-1] || btst[i+x]
			}
			if i-x-1 >= 0 {
				btst[i] = btst[i-x-1] || btst[i]
			}
		}

		if btst[n] {
			fmt.Fprintln(writer, "YES")
		} else {
			fmt.Fprintln(writer, "NO")
		}
	}
}
