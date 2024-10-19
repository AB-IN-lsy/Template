package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	in  = bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
)

func Read[T any]() T {
	var i T
	fmt.Fscan(in, &i)
	return i
}

const N int = 1e5 + 10

func solve() {

}

func main() {
	defer out.Flush()
	T := Read[int]()
	for T > 0 {
		solve()
		T--
	}
}
