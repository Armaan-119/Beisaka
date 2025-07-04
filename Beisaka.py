import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import time
from mouse_commands import handle_mouse_command
disambiguation_options = None
import webbrowser
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
import os
from button_use import press_button_command
from button_use import perform_shortcut
from screen_detector import describe_screen
import torch
from game_commands import execute_skyrim_command
import pyautogui
from chrome_shortcuts import * #(import * means important everything from the file)




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    else:
        speak ("good evening sir")
    
    speak("how can i help you today ")
 
    
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
        
    try:
        print('recognizing audio...')
        query = r.recognize_google(audio, language='en-in')
        print (f"user said: {query} \n")
        
    except Exception as e:
        print ("say that again please")
        speak("say that again please")
        return "None"
    return query

def get_wikipedia_summary(query):
    global disambiguation_options
    try:
        summary = wikipedia.summary(query, sentences=2)
        disambiguation_options = None  # Reset if successful
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        disambiguation_options = e.options[:5]  # Limit to 5 options
        return f"The term '{query}' is ambiguous. Did you mean: {', '.join(disambiguation_options)}?"
    except wikipedia.exceptions.PageError:
        return f"I couldn't find any page for '{query}'."
    except Exception as e:
        return f"An error occurred: {e}"
    


        

if __name__ == '__main__':
   #WishMe()
    while True:
        query = take_command().lower()
        if 'Beisaka' in query:
            print("yes ")
            speak("yes")
        elif "who are you" in query:
            print("my name is Beisaka")
            speak("my name is Beisaka")
        
        elif  "who created you" in query :
            print("i was created by ferrari")
            speak("i was created by ferrari")
            
        elif disambiguation_options and query.lower() in [opt.lower() for opt in disambiguation_options]:
            summary = get_wikipedia_summary(query)
            print(summary)
            speak(summary)
            continue  # Don't do any more processing this cycle

        
        elif "who is" in query or "what is" in query:
            query = query.replace("who is", "").replace("what is", "").strip()
            summary = get_wikipedia_summary(query)
            print(summary)
            speak(summary)
            
        elif "open google" in query:
                webbrowser.get(chrome_path).open('google.com')
                
        elif "open google and search" in query:
            speak('What should I search on Google?')
            qry = take_command().lower()
            search_url = f"https://www.google.com/search?q={qry}"
            webbrowser.get(chrome_path).open(search_url)

            try:
                results = wikipedia.summary(qry, sentences=1)
                speak(results)
            except Exception as e:
                speak("Sorry, I couldn't find information on that.")
                    
        elif "open youtube" in query:            
            webbrowser.get(chrome_path).open('https://www.youtube.com')

        elif "open youtube and search" in query:
            query = query.replace("open youtube and search", "").strip()
            if not query:
                speak("What should I search on YouTube?")
                query = take_command().lower()
            search_url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.get(chrome_path).open(search_url)
            
        elif "close browser" in query: 
            os.system("taskkill /f /im msedge.exe")
            
        
        elif "open notepad" in query:
            os.system("notepad.exe")
            
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

                
        elif "type" in query:
            query = query.replace("type", " ")
            pyautogui.typewrite(f"{query}", 0.1)
        
        elif "write" in query:
            query = query.replace("write", " ")
            pyautogui.typewrite(f"{query}", 0.1)
                
        elif "exit" in query or "quit" in query:
            speak("Goodbye, sir. Have a great day!")
            break
        
        elif "what can you see on the screen" in query or "describe screen" in query:
            describe_screen()
            
        elif "take a screenshot" in query:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot taken and saved as screenshot.png")
            
        elif "press" in query:
            press_button_command(query, speak=False)
        
        elif any(word in query for word in ["skyrim", "attack", "block", "sprint", "shout"]):
            execute_skyrim_command(query)

        elif perform_shortcut(query):
            pass  
    
        elif handle_mouse_command(query):
            pass  
        
        elif "tell me a joke" in query:
            speak("Why don't scientists trust atoms? Because they make up everything!")

        elif "what time is it" in query:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}")
            print(f"The current time is {current_time}")
            
        elif "what is the date today" in query:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"Today's date is {current_date}")
            print(f"Today's date is {current_date}")    
        
        elif handle_chrome_commands(query, speak):
            continue  
        
        elif "search" in query:
            search_query = query.replace("search", "").strip()
            if search_query:
                webbrowser.get(chrome_path).open(f"https://www.google.com/search?q={search_query}")
                speak(f"Searching for {search_query} on Google.")
            else:
                speak("What should I search for?")
                search_query = take_command().lower()
                webbrowser.get(chrome_path).open(f"https://www.google.com/search?q={search_query}")
                speak(f"Searching for {search_query} on Google.")
