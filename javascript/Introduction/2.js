'use strict';

let apple = '2', banana = '3';

console.log(Number(apple + banana)); //prints out 23 because it uses string binary operand and then conjugates into a string
console.log(Number(apple) + Number(banana)); //prints out 5 because it conjugates first and then uses binary operand

//unary plus and binus have priority over binary

console.log(+apple + +banana); //prints out 5 again

console.log('')
const APPLE_WORD = 'apple'
const BANANA_WORD = 'banana'

for (let x = 0; x < APPLE_WORD.length; x++){
    console.log(APPLE_WORD[x], BANANA_WORD[x])
}

console.log('')
for (let a = 0; a < 10; a++){
    console.log(a) //goes from 0 -> 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 : or rather 10 iterations
}

