const loginForm = document.querySelector("#login-form"); // 접근을 위한 변수

const loginInput = loginForm.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

const initBtn = document.querySelector("#init");

const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username"; // 반복되는 문자열을 사용할 때, 해당 문자열을 담을 변수를 지정해줌

function initClicked(){ // 초기화 함수화
    localStorage.removeItem(USERNAME_KEY);
    location.reload()
}

function onLoginSubmit(event){ // 브라우저가 자동으로 인자를 넘겨주는데, 이를 보통 함수에서 event로 명명함.
    event.preventDefault(); // 브라우저의 기본 동작을 막아줌. (submit시 새로고침 막음.)
    loginForm.classList.toggle(HIDDEN_CLASSNAME);// style.css에서 hidden 클래스를 가지고 있으면 사라지게 함. (submit후 사라짐)
    const username = loginInput.value;
    localStorage.setItem(USERNAME_KEY, username); // 로컬 저장소(웹의 저장소) 기능 활용, ("불러올 키워드", 저장할 인자)
    toggleGreeting();
}

function toggleGreeting(){ // 인사 창 함수화
    username = localStorage.getItem(USERNAME_KEY); // 로컬 저장소에서 저장된 이름 불러오기.
    greeting.innerText = `hello ${username}`; // string formating
    greeting.classList.toggle(HIDDEN_CLASSNAME); 
}

loginForm.addEventListener("submit", onLoginSubmit);
initBtn.addEventListener("click",initClicked);

const savedUsername = localStorage.getItem(USERNAME_KEY); // 유저 이름 저장 유무

if (savedUsername == null){
    loginForm.classList.toggle(HIDDEN_CLASSNAME);
}
else{
    toggleGreeting();
}