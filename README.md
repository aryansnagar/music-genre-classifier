# 🎶 Music Genre Classifier (Under Development)

A machine learning application that classifies the genre of music by listening through the device microphone.

---

## 📌 Overview
This project uses audio recording, mapping, and comparison techniques to predict the genre of music in real time.  
It is built with **Python**, using **Tkinter** for the GUI and **Matplotlib** for audio visualization.

---

## ⚙️ Application Structure
The application is divided into three main categories:

1. **Listener**  
   - Captures audio from the device microphone.  
   - Saves the recording as `recording.mp3`.  

2. **Mapper**  
   - Generates an audio map (spectrogram/visual representation) of the recorded sound.  
   - Displays the map using **Matplotlib**.  

3. **Comparator**  
   - Uses pre-existing tagged audio data for reference.  
   - Compares the new recording with the reference data.  
   - Assigns a predicted **genre tag** to the recording.  

---

## 🖥️ User Interface
- **GUI Framework**: Tkinter  
- **Audio Mapping**: Matplotlib  
- **Comparison Module**: Custom audio analysis with reference dataset  

---

## 🚧 Status
- Currently in **development phase**.  
- Modules are being integrated and tested.  

---

## 📜 License
This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.   
--- 
> 📝 This is my new college project, developed as part of my coursework.
