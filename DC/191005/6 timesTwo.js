const readline = require("readline");

const r1 = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function getAnswer(ans) {
  console.log("You answer x2 is: ");
  console.log(ans * 2);
  r1.close();
}

r1.question("Give me a number\n", getAnswer);
