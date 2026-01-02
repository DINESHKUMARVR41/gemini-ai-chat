async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  const msg = input.value;
  if (!msg) return;

  chatBox.innerHTML += `<div class="message user">${msg}</div>`;
  input.value = "";

  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg })
  });

  const data = await res.json();
  chatBox.innerHTML += `<div class="message ai">${data.reply}</div>`;
}
