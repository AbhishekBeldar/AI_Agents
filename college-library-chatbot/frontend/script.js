
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const sendButton = document.getElementById("send-button");

// Display a message in the chat window
function addMessage(message, sender) {
    const messageElement = document.createElement("div");

    messageElement.classList.add("message", sender);

    // Use textContent to safely display message text
    messageElement.textContent = message;

    chatBox.appendChild(messageElement);

    // Scroll to the latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Handle the form submission
chatForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const message = userInput.value.trim();

    if (message === "") {
        return;
    }

    // Display the user's message
    addMessage(message, "user");

    userInput.value = "";
    sendButton.disabled = true;

    try {
        // Send the question to the Python backend
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        if (!response.ok) {
            throw new Error("Could not get a response from the server.");
        }

        const data = await response.json();

        // Display the chatbot's reply
        addMessage(data.reply, "bot");

    } catch (error) {
        addMessage(
            "I could not connect to the chatbot server. Please make sure the Python backend is running.",
            "bot"
        );

        console.error("Chat error:", error);

    } finally {
        sendButton.disabled = false;
        userInput.focus();
    }
});
