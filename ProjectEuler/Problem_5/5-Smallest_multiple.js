// Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

let x = 19*17*13*11*7*5*3*2 //9699690

let found = false
while (!found) {
    for (let i = 1; i < 21; i++) {
        if (x % i) break
        else if (i == 20 && x % i == 0) {
            console.log(`Smallest multiple number is: ${x}`) //232792560
            found = true;
        }
    }
    x += 9699690
}
