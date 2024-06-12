package Java.Sorting;

import java.util.Scanner;

public class BubbleSort 
{
    public static void main(String[] args) 
    {
        int n;
        Scanner in = new Scanner(System.in);

        System.out.println("Enter size of array:");
        n = in.nextInt();

        int[] a = new int[n]; // declaring an array a of size n
        System.out.println("Enter array elements:");

        for (int i = 0; i < n; i++) // input array elements
            a[i] = in.nextInt();
        System.out.println("Updating class method");
        // Sorting the array using bubble sort
        bubbleSort(a);

        System.out.println("The sorted array is:");
        ArrayUtils.printArray(a);
    }

    // Method to perform bubble sort
    public static void bubbleSort(int[] arr) 
    {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) { // sorting in ascending order
                    // Swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}
class ArrayUtils extends BubbleSort 
{
    // Method to print an array
    public static void printArray(int[] arr) 
    {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}


public class OuterClass {
    private String outerField = "Outer field value";

    class InnerClass {
        public String innerMethod() {
            return "Inner class method called. Accessing: " + outerField;
        }
    }

    public void displayInner() {
        InnerClass inner = new InnerClass();
        System.out.println(inner.innerMethod());
    }

    public static void main(String[] args) {
        OuterClass outer = new OuterClass();
        outer.displayInner();
    }
}
