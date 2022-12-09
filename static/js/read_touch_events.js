const elementOne = document.getElementById("one");
const elementTwo = document.getElementById("two");
const elementThree = document.getElementById("three");
const elementFour = document.getElementById("four");
const elementFive = document.getElementById("five");
const elementSix = document.getElementById("six");
const elementSeven = document.getElementById("seven");
const elementEight = document.getElementById("eight");
const elementNine = document.getElementById("nine");
const elementTen = document.getElementById("ten");

const output = document.getElementById("output");
const clearer = document.getElementById("clear");

// functions

clearOutput = () => {
  output.value = "";
}

let logValue = [];

watchEvent = (element, eventName) => {
  element.addEventListener(eventName, e => {
//  e.preventDefault();
  logValue.push(element.id + " => " + eventName);
    if (eventName === "click") {
      output.value = output.value + logValue.join(" | ") + "\n";
      logValue = [];
    }
})
}

// Add event listeners

clearer.addEventListener("click", clearOutput);

//Init

watchEvent(elementOne, "click");
//watchEvent(elementOne, "focus");
//watchEvent(elementOne, "blur");
watchEvent(elementTwo, "click");
//watchEvent(elementTwo, "focus");
//watchEvent(elementTwo, "blur");
watchEvent(elementThree, "click");
//watchEvent(elementThree, "focus");
//watchEvent(elementThree, "blur");
watchEvent(elementFour, "click");
watchEvent(elementFive, "click");
watchEvent(elementSix, "click");
watchEvent(elementSeven, "click");
watchEvent(elementEight, "click");
watchEvent(elementNine, "click");
watchEvent(elementTen, "click");