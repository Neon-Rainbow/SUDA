package main

import "fmt"

func CalculateDifferentChar(left int, right int, target byte, s string) (ans int) {
	ans = 0
	for _, value := range s[left : right+1] {
		if byte(value) != target {
			ans++
		}
	}
	return
}

func CalculateMinimumChangesToMakeStringAGood(left int, right int, target byte, s string) (ans int) {
	if left == right {
		return CalculateDifferentChar(left, right, target, s)
	}
	mid := (left + right) / 2
	ans = min(
		CalculateMinimumChangesToMakeStringAGood(left, mid, target+1, s)+CalculateDifferentChar(mid+1, right, target, s),
		CalculateMinimumChangesToMakeStringAGood(mid+1, right, target+1, s)+CalculateDifferentChar(left, mid, target, s),
	)
	return
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var t int
	fmt.Scan(&t)

	for i := 0; i < t; i++ {
		var length int
		var s string

		fmt.Scan(&length)
		fmt.Scan(&s)

		ans := CalculateMinimumChangesToMakeStringAGood(0, length-1, 'a', s)
		fmt.Println(ans)
	}
}
