// MinMaxFinder.cs
using System;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            int[] numbers = { 5, 3, 9, 1, 4, 8, 2, 6, 7 };

            if (numbers.Length == 0)
            {
                Console.WriteLine("The array is empty.");
                return;
            }

            int min = FindMin(numbers);
            int max = FindMax(numbers);

            Console.WriteLine("Array elements: " + string.Join(", ", numbers));
            Console.WriteLine("Minimum value: " + min);
            Console.WriteLine("Maximum value: " + max);
        }
        catch (Exception ex)
        {
            Console.WriteLine("An error occurred: " + ex.Message);
        }
    }

    static int FindMin(int[] numbers)
    {
        int min = numbers[0];
        foreach (int number in numbers)
        {
            if (number < min)
            {
                min = number;
            }
        }
        return min;
    }

    static int FindMax(int[] numbers)
    {
        int max = numbers[0];
        foreach (int number in numbers)
        {
            if (number > max)
            {
                max = number;
            }
        }
        return max;
    }
}