// https://www.codewars.com/kata/duck-duck-goose/train/javascript
const duckDuckGoose = (players, goose) => {
  return players.map(player => player.name)[(goose - 1) % players.length];
};

// https://www.codewars.com/kata/reversed-strings/train/javascript/5a48d0d4b3bfa8e2cc00001c
const solution = str =>
  str
    .split("")
    .reverse()
    .join("");

// https://www.codewars.com/kata/swap-values/train/javascript
function swapValues() {
  let args = Array.prototype.slice.call(arguments);

  let temp = args[0][0]
  args[0][0] = args[0][1]
  args[0][1] = temp

  return args;
}