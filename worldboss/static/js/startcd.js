function startCountdown(elementId, datetimeId) {
    var datetime = document.getElementById(datetimeId).innerText;
    // Extract date and time components from datetime
    var regexPattern = /(\w+) (\d+), (\d+), (\d+):(\d+) (a.m.|p.m.)/i;
    var match = regexPattern.exec(datetime);
    var month = match[1];
    var day = match[2];
    var year = match[3];
    var hour = match[4];
    var minute = match[5];
    var amPm = match[6];
  
    // Adjust the hour value based on AM/PM
    if (amPm.toLowerCase() === "p.m." && hour !== "12") {
      hour = String(Number(hour) + 12);
    } else if (amPm.toLowerCase() === "a.m." && hour === "12") {
      hour = "0";
    }
  
    // Create a formattedDatetime string in "YYYY-MM-DD HH:mm:ss" format
    var formattedDatetime = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":00";
  
    formattedDatetime = formattedDatetime.toLocaleString("en-US", { timeZone: "America/New_York" });
  
    // Convert datetime to a JavaScript Date object
    var countDownDate = new Date(formattedDatetime).getTime();
  
    // Update the countdown every second
    var countdownTimer = setInterval(function() {
      // Get the current date and time
      var now = new Date().getTime();
  
      // Calculate the remaining time
      var distance = countDownDate - now;
  
      // Check if the countdown has ended
      if (distance < 0) {
        clearInterval(countdownTimer);
        document.getElementById(elementId).innerHTML = "Countdown expired";
      } else {
        // Calculate days, hours, minutes, and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
  
        // Display the countdown
        document.getElementById(elementId).innerHTML = hours + "h " + minutes + "m " + seconds + "s ";
      }
    }, 1000);
  }