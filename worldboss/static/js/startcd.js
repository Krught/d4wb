// function startCountdown(elementId, datetimeId) {
//     var datetime = document.getElementById(datetimeId).innerText;
//     // Extract date and time components from datetime
//     var regexPattern = /(\w+) (\d+), (\d+), (\d+):(\d+) (a.m.|p.m.)/i;
//     var match = regexPattern.exec(datetime);
//     var month = match[1];
//     var day = match[2];
//     var year = match[3];
//     var hour = match[4];
//     var minute = match[5];
//     var amPm = match[6];
  
//     // Adjust the hour value based on AM/PM
//     if (amPm.toLowerCase() === "p.m." && hour !== "12") {
//       hour = String(Number(hour) + 12);
//     } else if (amPm.toLowerCase() === "a.m." && hour === "12") {
//       hour = "0";
//     }
  
//     // Create a formattedDatetime string in "YYYY-MM-DD HH:mm:ss" format
//     var formattedDatetime = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":00";
  
//     var user_tz = document.getElementById("user-timezone").innerText;

//     formattedDatetime = formattedDatetime.toLocaleString("en-US", { timeZone: user_tz });
  
//     // Convert datetime to a JavaScript Date object
//     var countDownDate = new Date(formattedDatetime).getTime();
  
//     // Update the countdown every second
//     var countdownTimer = setInterval(function() {
//       // Get the current date and time
//       var now = new Date().getTime();
  
//       // Calculate the remaining time
//       var distance = countDownDate - now;
  
//       // Check if the countdown has ended
//       if (distance < 0) {
//         clearInterval(countdownTimer);
//         document.getElementById(elementId).innerHTML = "Countdown expired";
//       } else {
//         // Calculate days, hours, minutes, and seconds
//         var days = Math.floor(distance / (1000 * 60 * 60 * 24));
//         var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
//         var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
//         var seconds = Math.floor((distance % (1000 * 60)) / 1000);
  

//         // hours = formattedDatetime;
//         // Display the countdown
//         document.getElementById(elementId).innerHTML = hours + "h " + minutes + "m " + seconds + "s ";
//       }
//     }, 1000);
//   }
function startCountdown(elementId, datetimeId) {
  var datetime = document.getElementById(datetimeId).innerText;
  var regexPattern = /(\w+) (\d+), (\d+), (\d+):(\d+) (a.m.|p.m.)/i;
  var match = regexPattern.exec(datetime);
  var month = match[1];
  var day = match[2];
  var year = match[3];
  var hour = match[4];
  var minute = match[5];
  var amPm = match[6];

  if (amPm.toLowerCase() === "p.m." && hour !== "12") {
    hour = String(Number(hour) + 12);
  } else if (amPm.toLowerCase() === "a.m." && hour === "12") {
    hour = "0";
  }

    var formattedDatetime = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":00";
    formattedDatetime = day + "-" + month + "-" + year + " " + hour + ":" + minute + ":00";
    var user_tz = document.getElementById("user-timezone").innerText;



    var eventTime = moment(formattedDatetime, 'DD-MMMM-YYYY HH:mm:ss').unix()
    // currentTime = moment().unix(),
    // diffTime = eventTime - currentTime,
    // duration = moment.duration(diffTime * 1000, 'milliseconds'),
    // interval = 1000;

  // // if time to countdown
  // if(diffTime > 0) {

  //   setInterval(function(){

  //       duration = moment.duration(duration.asMilliseconds() - interval, 'milliseconds');
  //       var d = moment.duration(duration).days(),
  //           h = moment.duration(duration).hours(),
  //           m = moment.duration(duration).minutes(),
  //           s = moment.duration(duration).seconds();

  //       d = $.trim(d).length === 1 ? '0' + d : d;
  //       h = $.trim(h).length === 1 ? '0' + h : h;
  //       m = $.trim(m).length === 1 ? '0' + m : m;
  //       s = $.trim(s).length === 1 ? '0' + s : s;

  //       document.getElementById(elementId).innerHTML = h + "h " + m + "m " + s + "s ";

  //   }, interval);

  // } else {
  //   document.getElementById(elementId).innerHTML = "Countdown expired";
  // }

      var countdownTimer = setInterval(function() {
      var currentTime = moment().unix(),
      distance = eventTime - currentTime,
      duration = moment.duration(distance * 1000, 'milliseconds')
  
      // Check if the countdown has ended
      if (distance < 0) {
        clearInterval(countdownTimer);
        document.getElementById(elementId).innerHTML = "Countdown expired";
      } else {
        // Calculate days, hours, minutes, and seconds
        duration = moment.duration(duration.asMilliseconds(), 'milliseconds');
        var d = moment.duration(duration).days(),
            h = moment.duration(duration).hours(),
            m = moment.duration(duration).minutes(),
            s = moment.duration(duration).seconds();

        d = $.trim(d).length === 1 ? '0' + d : d;
        h = $.trim(h).length === 1 ? '0' + h : h;
        m = $.trim(m).length === 1 ? '0' + m : m;
        s = $.trim(s).length === 1 ? '0' + s : s;

        document.getElementById(elementId).innerHTML = h + "h " + m + "m " + s + "s ";
      }
    }, 1000);
  





}


