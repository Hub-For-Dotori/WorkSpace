const loginForm = document.querySelector("#login-form"); // 로그인 폼에 대한 정보 가져오기

const loginInput = loginForm.querySelector("#login-form input"); // 로그인 시, 입력 정보 받기
const greeting = document.querySelector("#greeting"); // 로그인 후, 인사 화면 출력할 정보 가져옴.

const initBtn = document.querySelector("#init"); // 초기화 버튼 만들어서 넣기.

const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username"; // 반복되는 문자열을 사용할 때, 해당 문자열을 담을 변수를 지정해줌

function initClicked(){ // 초기화 함수화
    localStorage.removeItem(USERNAME_KEY); // 로컬 저장소의 해당 데이터를 지움.
    location.reload(); // 초기화 후에 페이지 리로드 -> js를 처음부터 다시 읽어옴.
}

function onLoginSubmit(event){ // 브라우저가 자동으로 인자를 넘겨주는데, 이를 보통 함수에서 event로 명명함.
    event.preventDefault(); // 브라우저의 기본 동작을 막아줌. (submit시 새로고침 막음.)
    loginForm.classList.toggle(HIDDEN_CLASSNAME);// style.css에서 hidden 클래스를 가지고 있으면 사라지게 함. (submit후 사라짐)
    const username = loginInput.value; // 변수에 로그인 시 쓴 이름을 받아와서 저장함.
    localStorage.setItem(USERNAME_KEY, username); // 로컬 저장소(웹의 저장소) 기능 활용, ("불러올 키워드", 저장할 인자)
    toggleGreeting(); // 정보를 받아서 인사 창으로 넘어감.
}

function toggleGreeting(){ // 인사 창 함수화
    initBtn.classList.remove(HIDDEN_CLASSNAME); // 초기화 버튼 확실하게 뜨게 하기.
    username = localStorage.getItem(USERNAME_KEY); // 로컬 저장소에서 저장된 이름 불러오기.
    greeting.innerText = `hello ${username}`; // string formating
    greeting.classList.toggle(HIDDEN_CLASSNAME); // 인사 표시.
}

loginForm.addEventListener("submit", onLoginSubmit); // 이벤트 지정
initBtn.addEventListener("click",initClicked); 

const savedUsername = localStorage.getItem(USERNAME_KEY); // 유저 이름 저장 유무

if (savedUsername == null){ // 확실하게 보이고 감출 땐, toggle보다 add, remove를 쓰는게 좋을 것 같음.
    initBtn.classList.toggle(HIDDEN_CLASSNAME); // 초기 입력시 초기화 버튼 감춤.
    loginForm.classList.toggle(HIDDEN_CLASSNAME); // 초기 입력시 보이게 하기
}
else{
    toggleGreeting();
}