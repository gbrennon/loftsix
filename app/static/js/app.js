(function () {
    const questions = [
        'Como podemos te chamar?',
        'Quanto é 1+1?',
        'Quanto é 2+2?'
    ]

    const answers = [];
    let currentQuestionIdx = 0;

    const renderQuestion = (question) => {
        const template = `<li><p>${question}</p></li>`;
        const chatIteration = document.querySelector('.chat-iteration');

        return chatIteration.innerHTML += template;
    }

    const persistAnswer = (answer) => {
        const lastLi = document.querySelector('.chat-iteration li:last-child');
        const template = `<p>${answer}</p>`;

        return lastLi.innerHTML += template;
    }

    const answerQuestion = (event) => {
        event.preventDefault();
        const input = document.getElementById('chat-input');
        const answer = input.value;
        answers.push(answer);

        persistAnswer(answer);
        input.value = '';

        renderQuestion(questions[currentQuestionIdx]);
        currentQuestionIdx++;

        return false;
    }

    const answerForm = document.getElementById('answer-form');
    if (null != answerForm && undefined != answerForm) {
        answerForm.addEventListener('submit', answerQuestion);
    }
})();
