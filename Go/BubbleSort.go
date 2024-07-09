package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
)

/*
Sorts an array of integers using the bubble sort algorithm
*/

func main() {
	array := []int{}

	// Start from the index one because the zero contains the path of program
	for _, value := range os.Args[1:] {
		// Convert the parameter from string to integer
		number, err := strconv.Atoi(value)

		if err != nil {
			log.Fatal(err)
		}

		// Add number to array
		array = append(array, number)
	}

	fmt.Println("Unsorted array => ", array)
	fmt.Println("Sorted array => ", sort(array))
}

/*
I => -2 45 0 11 -9 3 92 88234 8 -14234 234 215 52
O => -14234 -9 -2 0 3 8 11 45 52 92 215 234 88234

Time complexity: O(n^2)
Space complexity: O(1)
*/
