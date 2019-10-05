const readline = require("readline");

const readALine = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function getAnswer(ans) {
  if (ans === "Y") {
    console.log("PIIIIIZZZAAA!");
  } else if (ans === "N") {
    console.log("Oh... ok :(");
  } else {
    console.log("Don't understand your answer...");
  }
  readALine.close();
}

readALine.question("Would you like a pizza? (Y/N))\n", getAnswer);
