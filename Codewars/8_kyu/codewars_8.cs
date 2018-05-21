// https://www.codewars.com/kata/duck-duck-goose/
public static string DuckDuckGoose(Player[] players, int goose)
{
    return players[(goose-1)%players.Length].Name;
}

// https://www.codewars.com/kata/keep-up-the-hoop/train/python/5ae0ebbac5a45243440000f7

public static string HoopCount(int n)
{
    return n>9 ? "Great, now move on to tricks" : "Keep at it until you get it";
}

// https://www.codewars.com/kata/reversed-strings/train/csharp
public static string Solution(string str) 
{
    return string.Join("",str.Reverse());
    //return new String(str.Reverse().ToArray());
}

// https://www.codewars.com/kata/the-feast-of-many-beasts/train/csharp
public static bool Feast(string beast, string dish)
{
    return beast[0] == dish[0] && beast[beast.Length-1] == dish[dish.Length-1];
}