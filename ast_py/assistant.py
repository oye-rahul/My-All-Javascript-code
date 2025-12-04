import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import subprocess
import time

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set voice properties (try different indices: 0 or 1)
try:
    engine.setProperty('voice', voices[1].id)  # Usually 1 for female, 0 for male
except:
    engine.setProperty('voice', voices[0].id)  # Fallback to first voice

engine.setProperty('rate', 150)  # Speech speed

def speak(text):
    """Make the assistant speak"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for voice command and convert to text"""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.pause_threshold = 1  # Wait 1 second after speech ends
        
        try:
            audio = recognizer.listen(source, timeout=5)
            print("🔍 Recognizing...")
            
            # Use Google's speech recognition
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"👤 You said: {query}")
            return query.lower()
            
        except sr.WaitTimeoutError:
            print("⏰ No speech detected")
            return "none"
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return "none"
        except sr.RequestError as e:
            print(f"❌ Error with speech recognition: {e}")
            return "none"

def open_application(app_name):
    """Open common applications"""
    apps = {
        'notepad': 'notepad.exe',
        'calculator': 'calc.exe',
        'paint': 'mspaint.exe',
        'file explorer': 'explorer.exe',
        'chrome': 'chrome.exe',
        'firefox': 'firefox.exe',
        'word': 'winword.exe',
        'excel': 'excel.exe'
    }
    
    if app_name in apps:
        try:
            subprocess.Popen(apps[app_name])
            speak(f"Opening {app_name}")
            return True
        except Exception as e:
            speak(f"Sorry, I couldn't open {app_name}")
            return False
    return False

def search_web(query, site=None):
    """Search the web or specific sites"""
    search_urls = {
        'youtube': 'https://www.youtube.com/results?search_query=',
        'google': 'https://www.google.com/search?q=',
        'wikipedia': 'https://en.wikipedia.org/wiki/'
    }
    
    if site in search_urls:
        url = search_urls[site] + query.replace(' ', '+')
    else:
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    webbrowser.open(url)
    speak(f"Searching {site if site else 'web'} for {query}")

def get_time():
    """Get current time"""
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")  # Format like 02:30 PM
    speak(f"The current time is {time_str}")

def get_date():
    """Get current date"""
    today = datetime.datetime.now()
    date_str = today.strftime("%A, %B %d, %Y")  # Format like Monday, January 01, 2024
    speak(f"Today is {date_str}")

def system_control(command):
    """Control system functions"""
    if 'shutdown' in command:
        speak("Shutting down the system in 10 seconds")
        os.system("shutdown /s /t 10")
    elif 'restart' in command or 'reboot' in command:
        speak("Restarting the system in 10 seconds")
        os.system("shutdown /r /t 10")
    elif 'lock' in command:
        speak("Locking the system")
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif 'sleep' in command:
        speak("Putting system to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def process_command(command):
    """Process the voice command and execute appropriate action"""
    
    if command == "none":
        return True  # Continue listening
    
    # Greetings
    if any(word in command for word in ['hello', 'hi', 'hey']):
        responses = ["Hello! How can I help you?", "Hi there!", "Hey! What can I do for you?"]
        speak(responses[datetime.datetime.now().second % 3])
    
    # Time queries
    elif 'time' in command:
        get_time()
    
    # Date queries
    elif 'date' in command:
        get_date()
    
    # Open applications
    elif 'open' in command:
        for app in ['notepad', 'calculator', 'paint', 'chrome', 'firefox', 'word', 'excel']:
            if app in command:
                open_application(app)
                break
        else:
            speak("Which application would you like me to open?")
    
    # Web searches
    elif 'search' in command:
        if 'youtube' in command:
            query = command.replace('search youtube for', '').replace('search on youtube', '').strip()
            search_web(query, 'youtube')
        elif 'google' in command:
            query = command.replace('search google for', '').replace('search on google', '').strip()
            search_web(query, 'google')
        elif 'wikipedia' in command:
            query = command.replace('search wikipedia for', '').replace('wikipedia', '').strip()
            search_web(query, 'wikipedia')
        else:
            query = command.replace('search for', '').replace('search', '').strip()
            search_web(query)
    
    # System control
    elif any(word in command for word in ['shutdown', 'restart', 'lock', 'sleep']):
        system_control(command)
    
    # Exit command
    elif any(word in command for word in ['exit', 'quit', 'goodbye', 'stop']):
        speak("Goodbye! Have a great day!")
        return False
    
    else:
        speak("I'm not sure how to help with that. Try asking me to open an app, search the web, or tell you the time.")
    
    return True  # Continue running

def main():
    """Main function to run the voice assistant"""
    speak("Voice Assistant activated. How can I help you today?")
    print("\n" + "="*50)
    print("🎯 Voice Assistant Started!")
    print("💡 Try saying: 'open notepad', 'what time is it', 'search youtube for cats'")
    print("🔚 Say 'exit', 'quit', or 'goodbye' to stop")
    print("="*50)
    
    running = True
    while running:
        command = take_command()
        running = process_command(command)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAssistant stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, I encountered an error. Restarting...")