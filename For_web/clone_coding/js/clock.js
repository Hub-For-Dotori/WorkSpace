const clock = document.querySelector("h2#clock");

function getClock(){
    const date = new Date(); // 시계 기능
    const hours = String(date.getHours()).padStart(2,"0"); // string으로 타입 캐스팅후, 포멧팅 (2글자 아래인 경우 앞에 "0"을 씀.(string에서 활용 가능))
    const minutes = String(date.getMinutes()).padStart(2,"0");
    const seconds = String(date.getSeconds()).padStart(2,"0");
    clock.innerText = `${hours}:${minutes}:${seconds}`;
}

getClock(); // 최초 호출해야함. 아래 코드에서 1초 간격으로 호출하므로.
setInterval(getClock, 1000); 
// setTimeout(sayHello, 1000); -> (실행 함수, 지연 호출 시간) 