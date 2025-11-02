
<h1 align="center">🕵️‍♂️ SpyCamSniffer</h1>
<p align="center">
  🔐 A stealthy Python tool to detect unauthorized access to your webcam in real-time.
</p>

⚠️ What is SpyCamSniffer?

*SpyCamSniffer* is a lightweight, open-source Python tool built for cyber security professionals, privacy-conscious users, and ethical hackers.

> 🧠 *Use Case:* Ever wondered if some app is secretly watching you through your webcam?  
> This tool *sniffs* for any silent intruders attempting to access your camera — and alerts you ⚡

---

🎯 Features

- ✅ Detects active webcam usage in real-time
- ⚠️ Warns you if your webcam is being used
- 🧩 Minimal resource usage
- 🧠 Easily extendable for mic/screen detection
- 💻 Runs on Windows, Linux & Mac (OpenCV-supported)

---

🛠 Installation

```bash
git clone https://github.com/karndeepbaror/SpyCamSniffer
cd SpyCamSniffer
pip install -r requirements.txt
```

---

🚀 Usage

```bash
python spycamsniffer.py
```

It will check every few seconds and alert you if the webcam is active!

---

📦 Requirements

All dependencies are listed in `requirements.txt`:

- `opencv-python`
