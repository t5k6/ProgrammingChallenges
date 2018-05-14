// https://www.codewars.com/kata/duck-duck-goose/
public static String duckDuckGoose(Player[] players, int goose) {
    return players[(goose-1)%players.length].name;
}