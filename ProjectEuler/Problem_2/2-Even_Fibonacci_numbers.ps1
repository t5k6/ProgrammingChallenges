[int]$num1 = 1
[int]$num2 = 1
[int]$sum = 0

DO  {
    $num1, $num2 = $num2, ($num1 + $num2)
    if (!($num2%2)) {
        $sum += $num2
    }
} While ($num2 -lt 4000000)
write-host $sum