package main

import (
	"fmt"
	"hello/hello/morestrings"

	"github.com/google/go-cmp/cmp"
)

func main() {
	fmt.Println(morestrings.ReverseRunes("!oG ,olleH"))

	fmt.Println(cmp.Diff("hello", "go"))
}
