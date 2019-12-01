(function() {
    let questions = [];
    const answers = [];
    let currentQuestionIdx = 0;

    const renderQuestion = (question) => {
        const template = `<li><p class="typewriter">${question}</p></li>`;
        const chatIteration = document.querySelector('.chat-iteration');

        return chatIteration.insertAdjacentHTML('beforeEnd', template);
    }

    const persistAnswer = (answer) => {
        const lastLi = document.querySelector('.chat-iteration li:last-child');
        const template = `<p>${answer}</p>`;
        answers.push(answer);

        return lastLi.innerHTML += template;
    }

    const answerQuestion = (event) => {
        event.preventDefault();
        const input = document.getElementById('chat-input');
        const answer = input.value;

        persistAnswer(answer);
        input.value = '';

        currentQuestionIdx++;
        renderQuestion(questions[currentQuestionIdx]);

        if(answers.length == questions.length) {
            return true;
        }

        return false;
    }

    const setupSurvey = (_questions) => {
        questions = _questions;
        console.log(questions);
        renderQuestion(questions[currentQuestionIdx]);
    };

    window.setupSurvey = setupSurvey;

    const answerForm = document.getElementById('answer-form');
    answerForm.addEventListener('submit', answerQuestion);
})();
