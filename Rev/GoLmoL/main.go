package main

import (
	"fmt"
	"log"
)

func main() {
    // Initial Flag
    flag := "PCTF{"

    // Get user input
    fmt.Println("++++++++++++++++++++")
    fmt.Println("Secret Please: ") 
    fmt.Println("++++++++++++++++++++")
    var userInput string 
    fmt.Scanln(&userInput)

    // Sekret Generation
    var sekret []string
    for i := 33; i < 123; i+=5 {
        data := fmt.Sprintf("%c", i)
        sekret = append(sekret, data)
    }

    // Comparing length of userinput with sekret
    if len(userInput) == len(sekret) {
        fmt.Println("++++++++++++++++++++")
        fmt.Println("Correct Flag Length -> Proceeding")
        fmt.Println("++++++++++++++++++++")
    } else {
        fmt.Println("-----------------------")
        log.Fatal("Wrong Flag Length")
    }

    // Compare userInput and sekret
    for i, _ := range sekret {
        if sekret[i] == string(userInput[i]) {
            flag += string(userInput[i]+7)
        } else {
            fmt.Println("-----------------------")
            log.Fatal("Wrong Flag")
            fmt.Println("-----------------------")
        }
    }
    fmt.Println("Congratulations")
    fmt.Println("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    fmt.Println(flag)
    fmt.Println("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
}
