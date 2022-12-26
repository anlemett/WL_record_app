var sound = document.getElementById("sound"); 

function playAudio() { 
    sound.play(); 
} 

function pauseAudio() { 
    sound.pause(); 
}

function soundAlert() { 
    alert("Hello"); 
}

document.getElementById("test").innerHTML = "TEST"; 

const elementStart = document.getElementById("start");
const elementStop = document.getElementById("stop");


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

 


watchEvent = (element, eventName) => {
  element.addEventListener(eventName, e => {

    if (eventName === "click") {
        ;
    }
})
}

watchEvent(elementStart, "click");
watchEvent(elementStop, "click");

watchEvent(elementOne, "click");
watchEvent(elementTwo, "click");
watchEvent(elementThree, "click");
watchEvent(elementFour, "click");
watchEvent(elementFive, "click");
watchEvent(elementSix, "click");
watchEvent(elementSeven, "click");
watchEvent(elementEight, "click");
watchEvent(elementNine, "click");
watchEvent(elementTen, "click");
