let categories = ["general_knowledge", "geography", "music", "history", "arts_and_literature", "sport_and_leisure", "food_and_drink", "society_and_culture"];
let usedCategories = [];
let currentPlayer = 1;
let currentQuestionIndex = 0;
let currentQuestions = [];
let scores = { player1: 0, player2: 0 };
let player1Name = '';
let player2Name = '';

async function fetchQuestions(category, difficulty) {
    try {
        const response = await fetch(`https://the-trivia-api.com/api/questions?categories=${category}&limit=2&difficulty=${difficulty}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching questions:', error);
        return [];
    }
}



function startSetup() {
    player1Name = document.getElementById('player1Name').value || 'Player 1';
    player2Name = document.getElementById('player2Name').value || 'Player 2';

    if (!player1Name || !player2Name) {
        alert("Please enter names for both players.");
        return;
    }

    document.getElementById('playerSetup').style.display = 'none';
    document.getElementById('categorySelection').style.display = 'block';
}

async function startGame() {
    const selectedCategory = document.getElementById('categoryDropdown').value;
    if (!selectedCategory || usedCategories.includes(selectedCategory)) {
        alert("Please select a valid and unused category.");
        return;
    }

    usedCategories.push(selectedCategory);

    // Fetch questions for each difficulty level
    const easyQuestions = await fetchQuestions(selectedCategory, 'easy');
    const mediumQuestions = await fetchQuestions(selectedCategory, 'medium');
    const hardQuestions = await fetchQuestions(selectedCategory, 'hard');

    // Combine all questions into a single array
    currentQuestions = [...easyQuestions, ...mediumQuestions, ...hardQuestions];
    currentQuestionIndex = 0;
    
    document.getElementById('categorySelection').style.display = 'none';
    document.getElementById('questionContainer').style.display = 'block';
    
    displayQuestion();
}


function displayQuestion() {
    if (currentQuestionIndex >= currentQuestions.length) {
        document.getElementById('questionContainer').style.display = 'none';
        document.getElementById('postQuestionOptions').style.display = 'block';
        return;
    }

    const question = currentQuestions[currentQuestionIndex];
    const difficulty = question.difficulty;
    const points = difficulty === 'easy' ? 10 : difficulty === 'medium' ? 15 : 20;

    document.getElementById('currentPlayer').textContent = `Player ${currentPlayer}'s turn`;
    document.getElementById('questionText').textContent = question.question;

    const answerOptions = document.getElementById('answerOptions');
    answerOptions.innerHTML = '';

    question.incorrectAnswers.concat(question.correctAnswer).forEach((answer) => {
        const li = document.createElement('li');
        li.textContent = answer;
        li.onclick = function () {
            if (answer === question.correctAnswer) {
                scores[`player${currentPlayer}`] += points;
                document.getElementById(`player${currentPlayer}Score`).textContent = scores[`player${currentPlayer}`];
            }
            nextQuestion();
        };
        answerOptions.appendChild(li);
    });
}

function nextQuestion() {
    currentPlayer = currentPlayer === 1 ? 2 : 1;
    currentQuestionIndex++;
    displayQuestion();
}

function selectAnotherCategory() {
    document.getElementById('postQuestionOptions').style.display = 'none';
    document.getElementById('categorySelection').style.display = 'block';
}

function endGame() {
    document.getElementById('postQuestionOptions').style.display = 'none';
    document.getElementById('gameOver').style.display = 'block';

    const player1Score = scores.player1;
    const player2Score = scores.player2;

    let resultText = `Player 1 (${player1Name}): ${player1Score}, Player 2 (${player2Name}): ${player2Score}. `;

    if (player1Score > player2Score) {
        resultText += "Player 1 wins!";
    } else if (player2Score > player1Score) {
        resultText += "Player 2 wins!";
    } else {
        resultText += "It's a tie!";
    }

    document.getElementById('finalScores').textContent = resultText;
}
