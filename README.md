# Voice-to-Voice Chatbot 

A simple voice-to-voice chatbot that records speech, sends the transcribed text to a Gemini model via google-generativeai, and speaks the model's reply using pyttsx3. Intended as a lightweight local demo for voice interaction with a generative model.

## Features
- Microphone input → speech-to-text (Google Speech Recognition)
- Sends user text to Gemini (via google.generativeai)
- Text-to-speech replies (pyttsx3)
- Minimal, single-file implementation for quick experimentation

## Requirements
- Python 3.8+
- Libraries: pyttsx3, SpeechRecognition, google-generativeai, (PyAudio or an alternative for microphone access)
- A valid generative AI API key (do not hardcode into the repo)

