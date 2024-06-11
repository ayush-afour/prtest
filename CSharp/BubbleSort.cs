using System;
					
public class Program
{
	public static void Main()
	{		
		int[] arrayInitial = { 100, 67, 95, 34, 1, 82, 23, 56, 74, 48, 99 };	
		Console.WriteLine("Array initial: " + Extensions.ArrayIntToString(arrayInitial));
		
		var sorted = new BubbleSort().Execute(arrayInitial);
		Console.WriteLine("Array sorted by Bubble Sort: " + Extensions.ArrayIntToString(sorted));
	}
}

public class BubbleSort
{
	public int[] Execute(int[] array)
	{
		int temp;
		
		foreach (int pos in array)
		{
			for (int i = 0; i <= array.Length - 2; i++) {
               if (array[i] > array[i + 1]) {
                  temp= array[i + 1];
                  array[i + 1] = array[i];
                  array[i] = temp;
               }
            }
		}	
		
		return array;
	}
}

public static class Extensions
{
	public static string ArrayIntToString(int[] array)
	{		
		var result = string.Empty;
		
		foreach (int pos in array)
			result += pos + " ";
		
		return result;
	}
}
class Program
{
    static void Main(string[] args)
    {
        try
        {
            Console.WriteLine("Enter a number to check if it's prime:");
            int number = int.Parse(Console.ReadLine());

            if (IsPrime(number))
            {
                Console.WriteLine($"{number} is a prime number.");
            }
            else
            {
                Console.WriteLine($"{number} is not a prime number.");
            }
        }
        catch (FormatException)
        {
            Console.WriteLine("Please enter a valid integer.");
        }
        catch (Exception ex)
        {
            Console.WriteLine("An error occurred: " + ex.Message);
        }
    }

    static bool IsPrime(int number)
    {
        if (number <= 1)
        {
            return false;
        }

        for (int i = 2; i <= Math.Sqrt(number); i++)
        {
            if (number % i == 0)
            {
                return false;
            }
        }

        return true;
    }
}
/*
 Input used: 100, 67, 95, 34, 1, 82, 23, 56, 74, 48, 99
 
 Expected Output: Sorted Array by Bubble Sort: 1 23 34 48 56 67 74 82 95 99 100
 
 Time Complexity: O(n^2) 
 Space Complexity: O(1)

*/