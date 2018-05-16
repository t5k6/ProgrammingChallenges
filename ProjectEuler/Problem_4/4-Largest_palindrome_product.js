// Find the largest palindrome made from the product of two 3-digit numbers.

let largest = 0

const palindrome = text => {
    return text == [...text].reverse().join('')
}

for (let i = 999; i > 900; i--) {
    for (let j = 999; j > 900; j--) {
        if (palindrome(''+(i * j)) && (i * j) > largest)
            largest = i*j    
    }
}

console.log(largest)