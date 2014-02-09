package main

import (
  "bufio"
  "fmt"
  "log"
  "os"
  "strconv"
  "strings"
)


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
      // Get the values
      vals :=  strings.Split(text, " ")
      f, _ := strconv.Atoi(vals[0])
      b, _ := strconv.Atoi(vals[1])
      length, _ := strconv.Atoi(vals[2])
      output := ""

      // Go through and find where things are mod of F & B
      for i := 1; i <= length; i++ {
        // To get things in the right format state
        if (i > 1) {
          output += " "
        }
        if (i % f == 0 && i % b == 0) {
          output += "FB"
        } else if(i % f == 0) {
          output += "F"
        } else if (i % b == 0) {
          output += "B"
        } else {
          output += strconv.Itoa(i)
        }
      }
      fmt.Println(output)
    }
    text,e = Readline(r)
  }
}