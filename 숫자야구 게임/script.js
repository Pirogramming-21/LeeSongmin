// 변수 초기화
let answer = [];
let attempts = 9;
let gameOver = false;

// 게임 초기화
function initGame() {
    answer = generateRandomNumbers();
    attempts = 9;
    gameOver = false;
    clearInputs();
    clearResults();
    document.querySelector('.submit-button').disabled = false;
    document.getElementById('game-result-img').src = '';
}

// 랜덤 숫자 생성
function generateRandomNumbers() {
    let numbers = [];
    while(numbers.length < 3) {
        let num = Math.floor(Math.random() * 10);
        if(!numbers.includes(num)) {
            numbers.push(num);
        }
    }
    return numbers;
}

// 입력 필드 초기화
function clearInputs() {
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
} 

// 결과 창 초기화
function clearResults() {
    document.querySelector('.result-display').innerHTML = '';
}