package main
import (
  "fmt"
  "os"
  "bufio"
  "log"
  "strings"
)

// doing own max function instead of importing math library.
func max(a int, b int) int {
  if a > b {
    return a
  }
  return b
}

// helpful function to read a line in go1 (codeEval version)
func Readline(r *bufio.Reader) (string, error) {
  var (isPrefix bool = true
       err error = nil
       line, ln []byte
      )
  for isPrefix && err == nil {
      line, isPrefix, err = r.ReadLine()
      ln = append(ln, line...)
  }
  return string(ln),err
}

/**
 *  Returns the string of the longest common subsequence of
 *  the two strings. It will use DP to build a 2D array of
 *  the words, find the length, then work backwards to get
 *  the characters.
 */
func longestSubsequence(a string, b string) string {
  aLen := len(a)
  bLen := len(b)

  L := make([][]int, aLen+1)
  for i := range L {
    L[i] = make([]int, bLen + 1)
  }
  
  // Use DP to find the max val.
  // Starting with 1's because go initializes to 0 already.
  for i := 1; i <= aLen; i++ {
     for j := 1; j <= bLen; j++ {
        if (a[i-1] == b[j-1]) {
          L[i][j] = L[i-1][j-1] + 1
        } else {
          L[i][j] = max(L[i-1][j], L[i][j-1])
        }
     }
   }

  // Go backwards through the array. Every time there
  // is a value change, add that letter to the list.
  // read the substring out from the matrix
  maxLen := L[aLen][bLen]
  returnString := make([]byte, maxLen)
  for x, y := aLen, bLen; x != 0 && y != 0; {
      if L[x][y] == L[x-1][y] {
        x -= 1
      } else if L[x][y] == L[x][y-1] {
        y -= 1
      } else {
        maxLen -= 1
        returnString[maxLen] = a[x-1]
        x -= 1
        y -= 1
      }
  }
  return string(returnString)
}


func main() {
  // Open file.
  fileName := os.Args[1]
  file, err := os.Open(fileName)
  if err != nil {
    log.Fatal(err)
  }
  r := bufio.NewReader(file)
  text, e := Readline(r)
  for e == nil {
    if (len(text) > 1) {
      parts := strings.Split(text, ";")
      fmt.Println(longestSubsequence(parts[0], parts[1]))
    }
    text,e = Readline(r)
  }
}
