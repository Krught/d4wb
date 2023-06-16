const loginToggle = document.querySelector('.login-toggle');
const loginFormContainer = document.querySelector('.login-form-container');

loginToggle.addEventListener('click', (e) => {
    e.preventDefault();
    loginFormContainer.classList.toggle('show');
});

// Get reference to the div element
var userServerMessage = document.getElementById('user_server_message');

// Set a timer for 5 seconds
setTimeout(function() {
// Hide the div element by setting the display property to "none"
userServerMessage.style.display = 'none';
}, 5000);


// Call the function for each element
startCountdown("countdown", "boss-est-timer");
startCountdown("countdown-min", "boss-min-timer");
startCountdown("countdown-max", "boss-max-timer");



  