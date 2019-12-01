(function() {
    const questions = [
        'Como podemos te chamar?',
        'Quanto é 1+1?',
        'Quanto é 2+2?'
    ]

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

        renderQuestion(questions[currentQuestionIdx]);
        currentQuestionIdx++;

        return false;
    }

    const answerForm = document.getElementById('answer-form');
    answerForm.addEventListener('submit', answerQuestion);
})();
