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
    let resultImg = document.getElementById('game-result-img');
    resultImg.src = '';
    resultImg.style.display = 'none';
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
    if(gameOver) return;

    let inputs = [
        document.getElementById('number1').value,
        document.getElementById('number2').value,
        document.getElementById('number3').value
    ];

    if (inputs.some(input => input === '')) {
        clearInputs();
        return;
    }

    let guess = inputs.map(Number);
    let result = checkGuess(guess);
    displayResult(guess, result);
    attempts--;

    if (result.strikes === 3) {
        endGame(true);
    } else if (attempts === 0) {
        endGame(false);
    }

    clearInputs();
}

// 추측한 숫자와 정답 비교
function checkGuess(guess) {
    let strikes = 0;
    let balls = 0;

    for(let i = 0; i < 3; i++) {
        if(guess[i] === answer[i]) {
            strikes++;
        } else if (answer.includes(guess[i])) {
            balls++;
        }
    }
    return { strikes, balls };
}

// 결과 표시
function displayResult(guess, result) {
    let resultDiv = document.createElement('div');
    resultDiv.className = 'check-result';

    let leftDiv = document.createElement('div');
    leftDiv.className = 'left';
    leftDiv.textContent = guess.join(' ');

    let rightDiv = document.createElement('div');
    rightDiv.className = 'right';

    if (result.strikes === 0 && result.balls ===0) {
        rightDiv.innerHTML = '<div class="out num-result">0</div>';
    } else {
        if (result.strikes > 0) {
            rightDiv.innerHTML += `${result.strikes} <div class="strike num-result">S</div>`;
        } 
        if (result.balls > 0 ) {
            rightDiv.innerHTML += `${result.balls} <div class="ball num-result">B</div>`;
        }
    }
    resultDiv.appendChild(leftDiv);
    resultDiv.innerHTML += ':';
    resultDiv.appendChild(rightDiv);

    document.querySelector('.result-display').prepend(resultDiv);
}


// 게임 종료
function endGame(isWin) {
    gameOver = true;
    document.querySelector('.submit-button').disabled = true;
    let resultImg = document.getElementById('game-result-img');
    resultImg.src = isWin ? 'success.png' : 'fail.png';
    resultImg.style.display = 'block';
}

// 게임 시작
window.onload = initGame;