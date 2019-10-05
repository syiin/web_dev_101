let anArray = [];

anArray.push(1);
anArray.push(2);
anArray.push(3);
anArray.push(4);

console.log(`0th item in the array is: ${anArray[0]}`);
console.log(`1st item in the array is: ${anArray[1]}`);
console.log(`2nd item in the array is: ${anArray[2]}`);
console.log(`3rd item in the array is: ${anArray[3]}`);

let poppedItem = anArray.pop();
console.log("\nPopped an array item!\n");
console.log(`3rd item in the array is: ${anArray[3]}`);
console.log(`The popped item was: ${poppedItem}`);
