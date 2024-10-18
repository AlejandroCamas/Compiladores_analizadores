document.addEventListener("DOMContentLoaded", function () {
    const display = document.getElementById("display");
    const buttons = document.querySelectorAll(
      ".number, .operator, .clear, .equal"
    );
  
    buttons.forEach((button) => {
      button.addEventListener("click", function () {
        if (this.classList.contains("clear")) {
          display.value = "";
        } else if (this.classList.contains("equal")) {
          try {
            display.value = eval(display.value);
          } catch (error) {
            display.value = "Error";
          }
        } else {
          display.value += this.textContent;
        }
      });
    });
  });
  