# Intelligent_Voice-Assistant
Python selenium project

**Voice Assistant Project: Wikipedia Search, YouTube Playback, and More**

This project is a Python-based voice assistant designed to make daily tasks easier and more interactive through voice commands. It combines several functionalities like Wikipedia information retrieval, YouTube video playback, news updates, weather information, random facts, and jokes to provide a seamless and engaging user experience. The assistant employs Natural Language Processing (NLP) for speech recognition and text-to-speech synthesis, allowing users to interact with it naturally.

### Key Features:
1. **Wikipedia Information Retrieval:**  
   Users can ask the assistant for information on any topic, and it will fetch the first paragraph from Wikipedia and read it aloud.

2. **YouTube Video Playback:**  
   The assistant can search YouTube for videos and play them directly in the browser.

3. **News Updates:**  
   Fetches the latest top headlines from a news API and reads them to the user.

4. **Weather Information:**  
   Provides real-time weather updates, including temperature and conditions, for the specified location.

5. **Random Facts:**  
   Shares interesting and fun facts to lighten the mood.

6. **Jokes:**  
   Tells a random joke using the Official Joke API to entertain the user.

7. **Voice Interaction:**  
   Uses `speech_recognition` to understand spoken commands and `pyttsx3` for speech synthesis to respond.

8. **Real-Time Responses:**  
   Incorporates Selenium WebDriver to dynamically fetch data from the web, ensuring up-to-date information.

### Technologies Used:
- **Libraries:** `speech_recognition`, `pyttsx3`, `randfacts`, `datetime`, `requests`, Selenium WebDriver.
- **APIs:** Wikipedia, News API, Official Joke API, OpenWeatherMap API.
- **Browser Automation:** Selenium for web-based operations like Wikipedia and YouTube.

### How It Works:
- The assistant starts by greeting the user with the date, time, and weather information.
- It listens for commands using a microphone and processes them using Google's speech recognition engine.
- Depending on the command, the assistant performs tasks like fetching information, playing videos, or sharing jokes and facts.
- The assistant speaks out results and displays them on the console for better user engagement.

This project showcases the integration of voice interaction with real-time web data, making it a powerful and user-friendly virtual assistant.
