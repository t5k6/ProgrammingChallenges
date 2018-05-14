let sum = 0
let x = y = 1
while (y < 4000000) {
    x = x ^ y
    y = y ^ x
    x = (x ^ y) + y
    if (y % 2 == 0) {
        sum += y
    }
}
console.log(sum);
