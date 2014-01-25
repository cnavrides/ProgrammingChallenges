package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
  	file, err := os.Open(os.Args[1])
  	if err != nil {
    	log.Fatal(err)
  	}
  	scanner := bufio.NewScanner(file)
  	// Go through each line of the file
  	for scanner.Scan() {
  		line := scanner.Text()
  		parts := strings.Split(scanner.Text(), ";")
  		fmt.Println(len(line))
  	}
}