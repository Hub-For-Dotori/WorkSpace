const a = 5;
const b = 2; // 상수 변수
let myName = "TW"; // 가변 변수
const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat"]; // 배열을 선언하는 방식은 비슷힘.

let player = { // object 지정, 안에 함수 지정도 가능. 기능을 모아둔 object일 경우 함수를 여기에 모아서 코드 간략화를 하는 것이 좋을 듯.
    name: "mm",
    Point: 10,
};

function sayHello(name){ // 함수 지정
    console.log("hello my name is " + name);
}

function muti(n1, n2){ // 함수 지정
   sum = n1 * n2;
   return sum;
}

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

document.title = "changed"; // html의 title 값 수정 가능. document 자체가 웹 사이트를 뜻함.(시작점)
console.log(document.location)
console.log(document.body)
console.log(document.title)
const titleName = document.getElementById("title"); // 태그안의 id, class 이름을 찾아서 가져오기 가능
console.dir(titleName) // 속성값 찾기 가능
title.innerText = "got you bro!!!"; // 얻은 속성값을 변경 할 수 있음.