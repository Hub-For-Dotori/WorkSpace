const imgs = [
    "0.jpeg",
    "1.jpeg",
    "2.jpeg",
];

const imageIndex = Math.floor(Math.random()*imgs.length);

const randomImage = imgs[imageIndex];

const bgImage = document.createElement("img"); // img 태그를 생성함.

bgImage.src = `img/${randomImage}`; // img 태그의 이미지 소스를 가져옴.

document.body.appendChild(bgImage); // html에 img 태그를 추가함.