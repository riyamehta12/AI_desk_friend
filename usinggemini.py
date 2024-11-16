import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import google.generativeai as genai

my_api = os.environ.get("GOOGLE_API_KEY")

if not my_api:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=my_api)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

chatStr = ""

engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-IN")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return None
def google_search(query):

    formatted_query = query.replace(' ', '+')
   
    url = f"https://www.google.com/search?q={formatted_query}"

    webbrowser.open(url)

def query_genai(prompt):
    try:
        response = model.generate_content([prompt])
        return response.text.strip()
    except Exception as e:
        print(f"Generative AI error: {e}")
        return None

def chat(query):
    global chatStr
    print(chatStr)
    
    chatStr += f"Riya: {query}\n Aibuddy: "
    try:
        response_text = query_genai(chatStr)
        if response_text:
            say(response_text)
            chatStr += f"{response_text}\n"
            return response_text
    except Exception as e:
        print(f"Generative AI error: {e}")
        return None

def ai(prompt):
    text = f"Generative AI response for Prompt: {prompt} \n *************************\n\n"
    try:
        response_text = query_genai(prompt)
        if response_text:
            text += response_text
            if not os.path.exists("GenerativeAI"):
                os.mkdir("GenerativeAI")
            with open(f"GenerativeAI/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
                f.write(text)
    except Exception as e:
        print(f"Generative AI error: {e}")

def search(query):
    prompt = f"Search for {query}"
    response = query_genai(prompt)
    return response

sites = [
    ["youtube", "https://www.youtube.com/"],
    ["wikipedia", "https://www.wikipedia.org/"],
    ["google", "https://www.google.com/"],
    ["github", "https://www.github.com/"],
    ["stackoverflow", "https://www.stackoverflow.com/"]
]

apps = {
    "notepad": "C:\\Windows\\System32\\notepad.exe",
    "spotify": "C:\\Users\\riya mehta\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe",
    "telegram": "C:\\Users\\riya mehta\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe",
    "whatsapp": "C:\\Users\\riya mehta\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
    "msword": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
}

say("Hello, I am just a girl")
while True:
    query = takecom()
    if query:
        for site in sites:
            if f"open {site[0]}" in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
                break
        else:
            if "open notepad" in query.lower():
                say("Opening Notepad")
                os.system(f'start {apps["notepad"]}')
            elif "open spotify" in query.lower():
                say("Opening Spotify")
                os.system(f'start {apps["spotify"]}')
            elif "open telegram" in query.lower():
                say("Opening Telegram")
                os.system(f'start {apps["telegram"]}')
            elif "open whatsapp" in query.lower():
                say("Opening WhatsApp")
                os.system(f'start {apps["whatsapp"]}')
            elif "open msword" in query.lower():
                say("Opening Microsoft Word")
                os.system(f'start {apps["msword"]}')
            elif "using artificial intelligence".lower() in query.lower():
                ai(prompt=query)
            elif "search" in query.lower():
                search_query = query.lower().replace("search on google", "").strip()
                say(f"Browsing the internet for {search_query}")
                google_search(search_query)
            elif "stop" in query.lower() or "exit" in query.lower():
                say("Goodbye!")
                break
            elif "reset chat" in query.lower():
                chatStr = ""
            else:
                response = chat(query)
                say(response)
                print(f"Generative AI response: {response}")
