// Find the largest palindrome made from the product of two 3-digit numbers.

const palindrome = text => text == [...text].reverse().join('')

let largest = 0

for (let i = 999; i > 900; i--) {
    for (let j = 999; j > 900; j--) {
        if (palindrome(''+(i * j)) && (i * j) > largest)
            largest = i*j    
    }
}

console.log(largest)