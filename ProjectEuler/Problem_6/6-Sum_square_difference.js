// Find the difference between the sum of the squares of the first one hundred 
// natural numbers and the square of the sum.

// Brute force method
let nSum = [...Array(101).keys()].reduce((a,n) => a + n, 0)
let sSum = [...Array(101).keys()].reduce((a,n) => a + n*n, 0)
console.log(nSum*nSum - sSum)  // 25164150

// Mathematical method
// (a + b + .. + n)^2     = n^2 * (n+1)^2 * 1/4
// (a^2 + b^2 + .. + n^2) = n * (n+1) * (2n+1) * 1/6
