// Create a socket connection with the server
var socket = io.connect();

// Get the user ID and exam ID from the HTML elements
var userId = document.getElementById('user-id').value;
var examId = document.getElementById('exam-id').value;

// Join the exam room with the user ID and exam ID
socket.emit('join', { user_id: userId, exam_id: examId });

// Listen for welcome messages from the server
socket.on('message', function (data) {
    // Display the welcome message to the user
    var messageBox = document.getElementById('message-box');
    messageBox.innerHTML = data;
});

// Listen for exam questions from the server
socket.on('question', function (data) {
    // Update the question and options on the page
    var questionBox = document.getElementById('question-box');
    questionBox.innerHTML = data.question;

    var optionsBox = document.getElementById('options-box');
    optionsBox.innerHTML = '';
    data.options.forEach(function (option) {
        var optionElem = document.createElement('div');
        optionElem.className = 'option';
        optionElem.innerText = option;
        optionElem.addEventListener('click', function () {
            // Send the selected answer to the server
            socket.emit('answer', { user_id: userId, exam_id: examId, answer: option });
        });
        optionsBox.appendChild(optionElem);
    });
});

// Listen for feedback messages from the server
socket.on('feedback', function (data) {
    // Display the feedback message to the user
    var feedbackBox = document.getElementById('feedback-box');
    feedbackBox.innerHTML = data;
});

// Listen for timer updates from the server
socket.on('timer', function (data) {
    // Update the timer display on the page
    var timerBox = document.getElementById('timer-box');
    timerBox.innerHTML = 'Time Remaining: ' + data + ' seconds';
});

// Listen for exam end messages from the server
socket.on('end', function (data) {
    // Display the exam end message to the user
    var endBox = document.getElementById('end-box');
    endBox.innerHTML = data;
});
