# Find the sum of all the multiples of 3 or 5 below 1000.
[int]$sum = 0
ForEach($i in 1..999){
    If (!($i%3) -Or !($i%5))
    {
        $sum += $i
    }
}
write-host $sum