const display = document.getElementById("display");
let num1 = "", num2 = "", op = "", current = "";

async function calculate(num1, op, num2) {
  const response = await fetch("/calculate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ num1, num2, operation: op })
  });
  const data = await response.json();
  return data.result;
}

async function handleKey(k) {
  if (k === "C") {
    num1 = op = current = num2 = "";
    display.textContent = "0";
    return;
  }
  if (["+", "-", "*", "/"].includes(k)) {
    if (num1 && op && current) {
      num2 = current;
      const res = await calculate(num1, op, num2);
      num1 = res;
      display.textContent = res;
      current = "";
    } else {
      num1 = current || "0";
      current = "";
    }
    op = k;
    return;
  }
  if (k === "=") {
    if (num1 && op && current) {
      num2 = current;
      const res = await calculate(num1, op, num2);
      display.textContent = res;
      num1 = res;
      current = "";
      op = "";
    }
    return;
  }
  // digits or decimal
  current += k;
  display.textContent = current;
}

document.querySelectorAll(".key").forEach(btn => {
  btn.addEventListener("click", () => handleKey(btn.dataset.key));
});
