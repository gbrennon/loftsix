(function() {
    let survey = [];
    let currentQuestionIdx = 0;

    const renderQuestion = (question) => {
        const template = `<li><p class="typewriter">${question}</p></li>`;
        const chatIteration = document.querySelector('.chat-iteration');

        return chatIteration.insertAdjacentHTML('beforeEnd', template);
    }

    const persistAnswer = (answer) => {
        const lastLi = document.querySelector('.chat-iteration li:last-child');
        const template = `<p>${answer}</p>`;

        survey[currentQuestionIdx].answer = answer;

        return lastLi.innerHTML += template;
    }

    const answerQuestion = (event) => {
        event.preventDefault();

        cleanTypewriterClass();
        const input = document.getElementById('chat-input');
        const answer = input.value;

        persistAnswer(answer);
        input.value = '';

        currentQuestionIdx++;

        if(survey.length == currentQuestionIdx) {
            return completeSurvey(survey);
        }

        renderQuestion(survey[currentQuestionIdx].question);

        return false;
    }

    const cleanTypewriterClass = () => {
        document.querySelector('.typewriter').classList.remove('typewriter');
    };

    const setupSurvey = (_survey) => {
        survey = _survey;
        renderQuestion(survey[currentQuestionIdx].question);
    };

    const completeSurvey = (survey) => {
        const surveyForm = document.querySelector('#survey-form');

        survey.forEach((question) => {
            const inputName = question.category;
            const input = document.querySelector(`input[name=${inputName}]`);

            input.value = question.answer;
        });

        setTimeout(() => {
            surveyForm.submit();
        }, 1000);
    };

    window.setupSurvey = setupSurvey;

    const answerForm = document.getElementById('answer-form');
    answerForm.addEventListener('submit', answerQuestion);
})();
