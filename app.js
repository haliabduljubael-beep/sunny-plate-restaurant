document.addEventListener("DOMContentLoaded", () => {
  const message = document.getElementById("order-message");
  document.querySelectorAll(".add-btn").forEach((button) => {
    button.addEventListener("click", () => {
      const foodName = button.dataset.name;
      message.textContent = `${foodName} added to your sample order!`;
    });
  });
});
