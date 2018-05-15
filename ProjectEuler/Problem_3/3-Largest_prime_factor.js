// What is the largest prime factor of the number 600851475143 ?
 
const check_prime = x => {
    for (let i = Math.floor(Math.sqrt(x) + 1); i > 3; i -= 2){
        if (x % i == 0 && is_prime(i))
            return i    
    }
}

const is_prime = x => {
    if (x < 2) return false
    if (x == 2 || x == 3 || x == 5) return true
    if (x % 2 == 0 || x % 3 == 0 || x % 5 == 0) return false
    for (let i = 3; i < Math.sqrt(x) + 1; i += 2){
        if (x % i == 0) return false
    }
    return true
}
console.log(is_prime(13))
console.log(check_prime(600851475143))