// 변수 초기화
let answer = [];
let attempts = 9;
let gameOver = false;

// 게임 초기화
function initGame() {
    answer = generateRandomNumbers();
    attempts = 9;
    clearInputs();
    clearResults();
    document.querySelector('.submit-button').disabled = false;
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

// 숫자 확인
function check_numbers() {
    let inputs = [
        document.getElementById('number1').value,
        document.getElementById('number2').value,
        document.getElementById('number3').value
    ];

    if (inputs.some(input => input === '')) {
        clearInputs();
        return;
    }

    let guess = imputs.map(Number);
    let result = checkGuess(guess);
    displayResult(guess, result);
    attempts--;

}

// 추측한 숫자와 정답 비교
function checkGuess(guess) {

}

// 결과 표시
function displayResult(guess, result) {

}

// 게임 종료
function endGame() {
    gameOver = true;
}