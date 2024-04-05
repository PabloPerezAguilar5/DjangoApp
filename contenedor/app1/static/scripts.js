document.addEventListener("DOMContentLoaded", function () {
  flatpickr("#hora", {
    enableTime: true,
    noCalendar: true,
    dateFormat: "H:i",
    minTime: "09:00",
    maxTime: "18:00",
    minuteIncrement: 15, // Esto limitará los minutos a 00, 15, 30 y 45
  });
});
