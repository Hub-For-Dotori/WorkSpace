const a = 5;
const b = 2; // 상수 변수
let myName = "TW"; // 가변 변수
const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat"]; // 배열을 선언하는 방식은 비슷힘.

//============================= object 조작 ===============================
let player = { // object 지정, 안에 함수 지정도 가능. 기능을 모아둔 object일 경우 함수를 여기에 모아서 코드 간략화를 하는 것이 좋을 듯.
    name: "mm",
    Point: 10,
};

//============================= 함수 조작 ===============================
function sayHello(name){ // 함수 지정
    console.log("hello my name is " + name);
}

function muti(n1, n2){ // 함수 지정
   sum = n1 * n2;
   return sum;
}
//============================= 입력 & 타입 캐스팅 ===============================

const age = parseInt(prompt("how old are you?")); // 페이지가 정지된 채로, 입력을 받음. (int형으로 받음)

if(isNaN(age)){
    console.log("please load again");
}
else{
    console.log("OK.");
}

console.log(a + b);
console.log(a - b);
console.log(a / b);
console.log(muti(a,b));
sayHello(myName);

//============================= 변수 조작 ===============================
myName = "Kwon";
sayHello(myName);
sayHello("butda");
console.log("My age is "+ age);
console.log(daysOfWeek);
daysOfWeek.push("sun"); // 배열에 요소를 맨 뒤에 추가함.
console.log(daysOfWeek);
console.log("today is " + daysOfWeek[0]);
console.log(player);
player.condition = "good"; // object에 새로운 요소 추가 가능
console.log(player);
console.log(player.name);
player.name = "KTW";
console.log(player.name);

//============================= html 조작 ===============================
document.title = "changed"; // html의 title 값 수정 가능. document 자체가 웹 사이트를 뜻함.(시작점)
console.log(document.location)
console.log(document.body)
console.log(document.title)
const titleName = document.getElementById("title"); // 태그안의 id 이름을 찾아서 가져오기 가능
console.dir(titleName) // 속성값 찾기 가능
title.innerText = "got you bro!!!"; // 얻은 속성값을 변경 할 수 있음. (바로 접근 가능.)
const helloMS = document.getElementsByClassName("hello"); // 태그안의 class 이름을 찾아서 가져오기 가능
console.dir(helloMS) // 속성값 찾기 가능

//============================= 이벤트 조작 ===============================
helloMS[0].innerText = "nice to meet you!!"; // 얻은 속성값을 변경 할 수 있음. (배열로 저장함.)

const h1 = document.querySelector(".hello"); // # -> id, . -> class
console.dir(h1); // 콘솔 창에서 이벤트들을 확인 가능함. (on~~ == 이벤트)
h1.innerText = "have a good time!!"

function handleH1Over(){ // 마우스가 h1에 있을 떄 기능
    console.log("title was over!");
    h1.innerText = "mouse on!";
    h1.style.color = "blue";// 색을 바꿔줌.
    h1.style.fontSize = '20px';// 폰트 크기 바꿔줌.
}
function handleH1Out(){ // 마우스가 h1에 없을 떄 기능
    console.log("title was out!");
    h1.innerText = "mouse out!";
    h1.style.color = "black";// 색을 바꿔줌.
    h1.style.fontSize = '12px'; // 폰트 크기 바꿔줌.
}
function handleH1Click(){ // 마우스가 h1에 없을 떄 기능
    console.log("mouse was clicked!");
    h1.innerText = "mouse was clicked!";
    h1.style.color = "red";// 색을 바꿔줌.
    h1.style.fontSize = '50px'; // 폰트 크기 바꿔줌.
}

h1.addEventListener("mouseover", handleH1Over);
h1.addEventListener("mouseout", handleH1Out); // h1에 어떤 행위를 했을 떄, 어떤 함수가 동작하게 하는지 쓰기 -> ("이벤트 타입", 함수명)
h1.addEventListener("click", handleH1Click);

//============================= 창 이벤트 조작 ===============================
function handleWindowResize(){
    document.body.style.backgroundColor = "gray";
}
function handleWindowOffline(){
    alert("Wifi unconnected!");
}
function handleWindowOnline(){
    alert("Wifi connected!");
}
window.addEventListener("resize", handleWindowResize);
window.addEventListener("offline", handleWindowOffline);
window.addEventListener("online", handleWindowOnline);
//h1.onclick(handleH1Click); <- 요거로도 가능함.
//h1.onmouseover(handleH1Over); <- 요거로도 가능함.
//h1.onmouseout(handleH1Out); <- 요거로도 가능함.

// getElementByTagName("태그명") -> 태그명으로 찾기 가능 
// querySelector(".클래스명 태그명") -> css방식으로 찾기 가능 (해당하는 첫번째 것만 가져옴)
// querySelectorAll(".클래스명 태그명") -> css방식으로 찾기 가능 (해당 사항 전부 가져옴)

//============================= css 이용 조작 ===============================
const title1 = document.querySelector("h1");

function handleDivH1Click(){
    /* 클래스를 날리고 구현하는 방법
    const clickedClass = "active";
    if (title1.className(clickedClass)){
        title1.className = clickedClass;
    }
    else {
        title1.className = clickedClass;
    }
    */

    /* 기존 클래스를 지우지 않고 구현하는 법
    const clickedClass = "active"
    if (title1.classList.contains(clickedClass)){
        title1.classList.remove(clickedClass);
    }
    else {
        title1.classList.add(clickedClass);
    }
    */
   title1.classList.toggle("active"); // 위 코드를 한 줄로 바꿈. on/off 스위치처럼 사용가능
}

title1.addEventListener("click", handleDivH1Click)