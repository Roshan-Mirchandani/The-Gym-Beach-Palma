document.addEventListener("DOMContentLoaded", function () {
  const messagesJson = document.getElementById("messages_json").textContent.trim();
  console.log(messagesJson);
  // Initialize the messages array
  let djangoMessages = [];

  try {
    // Parse the JSON content inside the <script> tag
    djangoMessages = JSON.parse(messagesJson);
  } catch (error) {
    console.error("Error parsing messages JSON:", error);
  }
  if (djangoMessages.length > 0) {
    const modal = document.getElementById("message_modal");
    const modal_message = document.getElementById("modal_message");

    modal_message.textContent = djangoMessages[0];
    modal.classList.remove("hidden");

    const close_btn = document.getElementById("close_btn");
    close_btn.addEventListener("click", function () {
      modal.classList.add("hidden");
    });
  }
});
// if(messages) {window.djangoMessages =  messages|safe } else{ []};
