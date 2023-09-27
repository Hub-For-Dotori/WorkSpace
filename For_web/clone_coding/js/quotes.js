const quotes = [
    { // 01번
        quote: "삶은 당신이 잠들지 못할 떄 벌어지는 일이다.",
        author: "프란 레보비츠",
    },
    { // 02번
        quote: "인간은 선천적으로는 거의 비슷하나 후천적으로 큰 차이가 나게 된다.",
        author: "공자",
    },
    { // 03번
        quote: "인생에서 원하는 것을 얻기 위한 첫 번째 단계는 내가 무엇을 원하는지 결정하는 것이다.",
        author: "벤 스타인",
    },
    { // 04번
        quote: "우리는 젊을 떄에 배우고, 나이가 들어서 이해한다.",
        author: "마리 폰 에브너 에센바흐",
    },
    { // 05번
        quote: "실천이 말보다 낫다.",
        author: "벤자민 프랭클린",
    },
    { // 06번
        quote: "배우지만 생각하지 않으면 공허하고, 생각하지만 배우지 않으면 위험하다.",
        author: "공자",
    },
    { // 07번
        quote: "완벽함이 아니라 탁월함을 위해 애써라.",
        author: "H. 잭슨 브라운 주니어",
    },
    { // 08번
        quote: "가장 위대한 영광은 한 번도 실패하지 않음이 아니라, 실패할 때마다 다시 일어서는 데에 있다.",
        author: "공자",
    },
    { // 09번
        quote: "삶이 있는 한, 희망은 있다.",
        author: "키케로",
    },
    { // 10번
        quote: "건강한 육체에 건강한 정신이 깃든다.",
        author: "유베날리스",
    },
];
const quote = document.querySelector("#quote span:first-child"); //id: quote -> tag: span의 첫 번째 자식
const author = document.querySelector("#quote span:last-child");

const quoteIndex = Math.floor(Math.random()*quotes.length); // 인덱스 지정 해줌.

const randomQuotes = quotes[quoteIndex]; // 랜덤 명언을 가져옴.

quote.innerText = randomQuotes.quote;
author.innerText = randomQuotes.author;