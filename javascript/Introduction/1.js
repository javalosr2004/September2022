"use strict";

function print(string){
    console.log(string)
}


function usingBigInt(){
    //allows us to store values larger / smaller than ±(2^53-1)
    let bigInt = 1234567890123456789012345678901234567890n; //the n at the end represents that it is BigInt
    print('hello world');

}

//you can embed functions or string into other strings

let example_name = 'John';

let example_string = `My name is ${example_name}`;

//find the type of a argument

console.log(typeof example_name) //returns string

console.log(typeof(example_name)) //also returns string

let name = prompt('Name', '');

let confirmation = confirm(`You are ${name}?`);

if (name == 'Johnny'){
    alert(`HIIIII ${name}, we've been expecting you.`)
}


let x = 1, y = 5

x = -x //this counts as unary operand because it only has a single operand

console.log(y - x) //this counts as a binary operand because it has two

let example_conversion = 20

example_conversion = String(example_conversion) //converts 20 into "20"


let apple = '2', banana = '3'

console.log(Number(apple + banana))

/*
String
Number
Boolean
*/

/*
Operators:

    Addition +,
    Subtraction -,
    Multiplication *,
    Division /,
    Remainder %,
    Exponentiation **.

*/