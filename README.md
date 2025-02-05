# Aibuddy: Your AI Assistant

This Python script implements a voice-activated AI assistant named Aibuddy. It leverages speech recognition, text-to-speech, web browsing, and Google's Gemini generative AI model to interact with the user and perform various tasks.

## Features

* **Voice Interaction:** Uses speech recognition to understand user commands and text-to-speech to provide responses.
* **Web Browsing:** Opens specified websites like YouTube, Wikipedia, Google, GitHub, and Stack Overflow.
* **Application Launching:** Launches applications like Notepad, Spotify, Telegram, WhatsApp, and Microsoft Word.
* **Generative AI Integration:** Uses Google's Gemini model for conversational AI, answering questions, and generating text based on prompts.  It also saves the AI generated content to text files.
* **Google Search:** Performs Google searches based on user queries.
* **Chat History:** Maintains a chat history for context in conversations (can be reset).
* **Error Handling:** Includes error handling for speech recognition and the Gemini API.

## Requirements

* Python 3.x
* `speech_recognition`
* `pyttsx3`
* `webbrowser`
* `google.generativeai`
* A Google API key (set as the `GOOGLE_API_KEY` environment variable)

## Installation

1.  **Clone the repository (Optional):** If you're using Git, you can clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Aibuddy.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/Aibuddy.git)  # Replace with your repo URL
    cd Aibuddy
    ```

2.  **Install the required packages:**
    ```bash
    pip install speech_recognition pyttsx3 google-generativeai
    ```

3.  **Set up your Google API key:**
    *   Obtain a Google API key from the Google Cloud Console.
    *   Set the `GOOGLE_API_KEY` environment variable.  How you do this depends on your operating system.  For example, in Linux/macOS:
        ```bash
        export GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY"
        ```
        In Windows:
        ```powershell
        $env:GOOGLE_API_KEY = "YOUR_ACTUAL_API_KEY"
        ```
        Or you can set it permanently in your system's environment variables settings.

## Usage

1.  Run the script:
    ```bash
    python your_script_name.py  # Replace with the actual name of your Python file
    ```

2.  Interact with Aibuddy using voice commands.  Some examples:

    *   "Open YouTube"
    *   "Open Notepad"
    *   "Search on Google for Python programming"
    *   "Using artificial intelligence, write a short story about a robot."
    *   "What is the capital of France?" (for conversational AI)
    *   "Stop" or "Exit" to quit.
    *   "Reset chat" to clear the conversation history.

## Code Overview

*   `takecom()`: Handles speech recognition.
*   `say()`: Handles text-to-speech.
*   `google_search()`: Opens Google searches in the browser.
*   `query_genai()`: Interacts with the Gemini API.
*   `chat()`: Manages the conversational AI aspect.
*   `ai()`: Handles AI prompts and saves the response to a file.
*   `search()`: Performs searches using the Gemini API.
