// What is the 10001st prime number?

const is_prime = x => {
    if (x < 2) return false
    if (x == 2 || x == 3 || x == 5) return true
    if (x % 2 == 0 || x % 3 == 0 || x % 5 == 0) return false
    for (let i = 3; i < Math.sqrt(x) + 1; i += 2){
        if (x % i == 0) return false
    }
    return true
}

let i = 2
let n = 0

while (n != 10001) {
    if (is_prime(i)) n += 1
    i += 1
}

console.log(i-1)  // 104743