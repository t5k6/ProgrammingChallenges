// https://www.codewars.com/kata/binary-addition/train/csharp/5ad8f17f32d79e747f0001e0
public static string AddBinary(int a, int b)
{
    return Convert.ToString((a+b), 2);
}

// https://www.codewars.com/kata/make-a-function-that-does-arithmetic/train/csharp
public static double Arithmetic(double a, double b, string op) 
{
    switch (op)
    {
        case "add":
            return a+b;
        case "subtract":
            return a-b;
        case "multiply":
            return a*b;
        case "divide":
            return a/b;
        default:
            return -1;
    }
}

// https://www.codewars.com/kata/number-of-divisions/train/csharp
public static int Divisions(int n, int divisor)
{
    return (int) ( Math.Log(n) / Math.Log(divisor) );
}

// https://www.codewars.com/kata/vowel-count/train/csharp
public static int GetVowelCount(string str)
{
    return str.Where( l => "aeoui".Contains(l)).ToArray().Length;
    // better: str.Count(i => "aeiou".Contains(i));
}