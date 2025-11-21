<!-- 🎙️ Molly the AI Assistant 🎙️ -->

<p align="center"></p>
<h1 align="center">🤖 Molly the AI Voice Assistant</h1>
<p align="center">
  <i>“Hello, I’m Molly the smart voice assistant powered by Gemini Pro and OpenAI!”</i><br>
  <b>Your voice-enabled AI buddy for chatting, helping, and exploring ideas with sound and text.</b>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-green.svg" alt="Python">
  <img src="https://img.shields.io/badge/Google-GenerativeAI-blue.svg" alt="Google Gem Pro">
  <img src="https://img.shields.io/badge/SpeechRecognition-robust.svg" alt="SpeechRecognition">
  <img src="https://img.shields.io/badge/PyGame-Audio-orange.svg" alt="PyGame">
</p>

---

## 🤖 Meet Molly Your Voice-Powered AI Companion


Molly is an intelligent AI assistant that listens to you and talks back, built on Google’s Gemini Pro large language model with OpenAI-powered text-to-speech.  
Mainly activated by voice through the wake phrase “Molly,” it also supports chat interactions.

- 🎙️ **Voice Activation:** Just say “Hello Molly” to wake her up and start talking naturally.  
- 💬 **Chat & Voice:** Type or speak your requests and get smart, conversational AI responses.  
- 🔊 **Natural TTS:** Molly speaks responses aloud using OpenAI TTS or local pyttsx3 synthesis for smooth dialogue.  
- 📝 **Conversation Logs:** All interactions are saved with timestamps in daily log files for review.  
- 🎛️ **Robust and Responsive:** Designed to work reliably with ambient noise adjustment and graceful error handling.

---

## ⚡ Features

- **Wake word detection:** Molly listens actively but responds only when called by name.  
- **Streaming AI replies:** Responses come streaming chunk-by-chunk for dynamic interaction.  
- **Multi-modal input:** Talk directly or type (optional enhancement).  
- **Configurable TTS:** Switch between cloud-based OpenAI audio or local speech synthesis.  
- **Logging:** Timestamps and conversation history saved to daily logs automatically.

---

## 🛠️ Molly’s Toolkit - Installation Guide

<em>"Get Molly ready to chat with you in no time!"</em>

**Step 1:** Install Python 3.8 or higher if not installed.

**Step 2:** Clone or download this project to your workspace.

**Step 3:** Open your terminal or VS Code integrated terminal and navigate to the project folder.

**Step 4:** (Recommended) Create and activate a virtual environment.

- On Windows:
   python -m venv venv
  .\venv\Scripts\activate

- On Mac/Linux:
  python3 -m venv venv
  source venv/bin/activate


**Step 5:** Install dependencies:
  pip install google-generativeai speechrecognition pyaudio pyttsx3 pygame openai

> 📌 **Note:**  
> Installing `pyaudio` may require additional system packages such as PortAudio.  
> For Windows, pre-built wheels for PyAudio are available online if installation issues arise.

---

## 🎬 How to Wake Molly and Start Talking

Open your terminal in the project folder and run:
  python molly.py


- Speak “Hello Molly” to activate voice interaction.  
- Ask questions, give commands, or just chat naturally.  
- Say “that’s all” or “goodbye” to let Molly sleep again.  

---

## 👩‍🔬 For Curious Techies

Want more? Add a GUI button, extend with multi-language support, or integrate even more advanced APIs.  
Use Molly for productivity, accessibility, creative experiments, or just for fun!

> “Call out to Molly and let your ideas spark she’s ready to listen, help, and chat with you!”  
>  Your friendly neighborhood voice assistant

---

<h3 align="center">🤖 Enjoy Chatting with Molly!</h3>
<p align="center"><i>“Molly listens, replies, and remembers your words. Try it and see!”</i></p>
<p align="center">Made with Python by Mohammed Sultan</p>
<p align="center">
  <img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="Built with Love">
  <img src="https://forthebadge.com/images/badges/powered-by-coffee.svg" alt="Powered by Coffee">
</p>
