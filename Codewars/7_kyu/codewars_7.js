// https://www.codewars.com/kata/ad2070-help-lorimar-troubleshoot-his-robots-ultrasonic-distance-analysis/train/javascript
function sensorAnalysis(sensor_data){
  let distances = sensor_data.map(s => s[1]);
  let mean = distances.reduce((prev, curr) => prev + curr) / distances.length;
  let deviations = distances.map(d => Math.pow((d - mean), 2)).reduce((prev, curr) => prev + curr);
  let std_dev = Math.sqrt(deviations / (sensor_data.length - 1));

  return [+mean.toFixed(4), +std_dev.toFixed(4)];
}

// https://www.codewars.com/kata/alternate-capitalization/train/javascript
const capitalize = s => {
  return [1,0].map(odd=>[...s].map((l,i) => i%2==odd ? l : l.toUpperCase()).join(''))
}

// https://www.codewars.com/kata/coding-meetup-number-2-higher-order-functions-series-greet-developers/train/javascript/5ad38db65c76bf13d7000123
function greetDevelopers(list) {
  list.forEach(function(item) {
    let message =
      "Hi " +
      item.firstName +
      ", what do you like the most about " +
      item.language +
      "?";
    item.greeting = message;
  });
  return list;
}

// https://www.codewars.com/kata/coding-meetup-number-3-higher-order-functions-series-is-ruby-coming/train/javascript/5ad39e375c76bf1915000135
const isRubyComing = list => list.some(item => item.language == "Ruby");

// https://www.codewars.com/kata/coding-meetup-number-4-higher-order-functions-series-find-the-first-python-developer/train/javascript/5ad3a0556b343b9cb5000256
function getFirstPython(list) {
  if (list.some(item => item.language == "Python")) {
    return list
      .filter(item => item.language == "Python")
      .map(item => item.firstName + ", " + item.country)[0];
  }
  return "There will be no Python developers";
}

// https://www.codewars.com/kata/coding-meetup-number-5-higher-order-functions-series-prepare-the-count-of-languages/train/javascript/5ad4a05aebbe5424fa00013e
const countLanguages = list => {
  let langs = list.map(item => item.language);
  return langs.reduce((tally, lang) => {
    tally[lang] = (tally[lang] || 0) + 1;
    return tally;
  }, {});
};

// https://www.codewars.com/kata/coding-meetup-number-6-higher-order-functions-series-can-they-code-in-the-same-language/train/javascript/5ad4bdc12fdf9159e7000030
const isSameLanguage = list => {
  let languages = list.map(item => item.language);
  return [...new Set(languages)].length == 1;
};

// https://www.codewars.com/kata/coding-meetup-number-11-higher-order-functions-series-find-the-average-age/train/javascript/5ada125536257fd7f700009c
const getAverageAge = list =>
  Math.round(
    list.map(item => item.age).reduce((n, p) => n + p, 0) / list.length
  );

// https://www.codewars.com/kata/coding-meetup-number-12-higher-order-functions-series-find-github-admins/train/javascript
const findAdmin = (list, lang) => {
  return list.filter(
    ({ language, githubAdmin }) => githubAdmin == "yes" && language == lang
  );
};

// https://www.codewars.com/kata/coding-meetup-number-14-higher-order-functions-series-order-the-food/train/javascript
const orderFood = list => {
  return list.reduce((r,v) => ({...r, [v.meal]: (r[v.meal] || 0) + 1}), {})
}

// https://www.codewars.com/kata/complementary-dna/train/javascript
const DNAStrand = dna => {
  dna_comp = { A: "T", T: "A", G: "C", C: "G" };
  return [...dna].map(item => dna_comp[item]).join("");
};

// https://www.codewars.com/kata/debug-the-functions-easy/train/javascript/5adf69316edb07c66300000d
function multi(arr) {
  return arr.reduce((a, b) => a * b, 1);
}
function add(arr) {
  return arr.reduce((a, b) => a + b, 0);
}
function reverse(str) {
  return str
    .split("")
    .reverse()
    .join("");
}

// https://www.codewars.com/kata/exes-and-ohs/train/javascript
const XO = str => count(str, "x") == count(str, "o");
const count = (str, letter) =>
  str.split("").filter(i => i.toLowerCase() == letter).length;

// https://www.codewars.com/kata/indexed-capitalization/train/javascript
function capitalize(s,arr){
  return [...s].map((el,i) => arr.includes(i) ? el.toUpperCase() : el).join('')
};

// https://www.codewars.com/kata/inspiring-strings/train/javascript
const longestWord = s => s.split(" ").reduce((a,b) => (a.length>b.length) ? a : b, [])

// https://www.codewars.com/kata/jaden-casing-strings/
String.prototype.toJadenCase = function() {
  let sCopy = this[0].toUpperCase();
  for (let i = 1; i <= this.length; i++) {
    if (i < this.length && this[i - 1] == " ") {
      sCopy += this[i].toUpperCase();
    } else if (i < this.length && this[i - 1] != " ") {
      sCopy += this[i];
    }
  }
  return sCopy;
};

// https://www.codewars.com/kata/list-filtering/train/javascript
const filter_list = l => l.filter(i=>typeof i === 'number')

// https://www.codewars.com/kata/make-a-function-that-does-arithmetic/train/python/5adb490ee7dbc462c60005bd
const arithmetic = (a, b, operator) =>
  ({
    add: a + b,
    subtract: a - b,
    multiply: a * b,
    divide: a / b
  }[operator]);

// https://www.codewars.com/kata/mumbling/train/javascript
const accum = s => {
  let ns = "";
  for (let e of s.split("").entries()) {
    ns += "-" + e[1].toUpperCase() + e[1].toLowerCase().repeat(e[0]);
  }
  return ns.slice(1);
};

// https://www.codewars.com/kata/number-of-divisions/train/javascript
const divisions = (n, divisor) => {
  if (n<divisor) return 0
  const helper = (n,d, s) => n/d >= d ? helper(n/d,d,s+1) : s
  return helper(n, divisor, 1)
};

// Mathematical solution:
// Math.floor(Math.log(n) / Math.log(divisor))

// https://www.codewars.com/kata/ones-complement/train/javascript
const onesComplement = n => [...n].map(i=> i^1).join('')

// https://www.codewars.com/kata/pull-your-words-together-man/train/javascript
function sentencify(words) {
  return (words.join(' ')).replace(/^\w/g, l => l.toUpperCase()) + '.'
}

// https://www.codewars.com/kata/regex-validate-pin-code/train/javascript
const validatePIN = pin => /^[\d]{4}([\d]{2})?$/.test(pin)
// matches 4 or 6 digit PIN codes {2} is 6-4 => 2 more from already found 4

// https://www.codewars.com/kata/square-every-digit/train/javascript
function squareDigits(num){
  return +[...(''+num)].map(i=>+i*+i).join('')
}

// https://www.codewars.com/kata/turn-any-word-into-a-beef-taco/train/javascript
function tacofy(word) {
  let tacoD = {t: "tomato", l: "lettuce", c: "cheese", g: "guacamole", s: "salsa"}
  let vowels = "aeiou"
  let ingredients = [...word.toLowerCase()].map(i=> tacoD[i] ? tacoD[i] : vowels.includes(i) && "beef").filter(i=>i)
  return ['shell',...ingredients, 'shell']
}

// https://www.codewars.com/kata/vowel-count/train/javascript
const getCount = str => str.split("").filter(x => "aeiou".includes(x)).length;
