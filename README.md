# 🐾 Animal Detection and Alert System

A real-time **animal detection system** using **YOLOv12x**, **OpenCV**, and **Twilio SMS API**.  
It detects animals from a webcam feed and sends an **SMS alert** when an animal is spotted.  

---

## 🚀 Features
- Live video stream analysis with **YOLOv12x**.
- Detects common animals (cats, dogs, cows, elephants, birds, etc.).
- Sends **SMS alerts via Twilio** — only once per detected animal to prevent spam.
- Bounding boxes drawn on detected animals in real time.

---

## 📂 Project Structure
```.
├── main.py # Core detection script
├── .env # Environment variables (Twilio credentials & phone numbers)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/sahitya1903/animal-detection-alert.git
cd animal-detection-alert
```

### 2. Create a virtual environment (recommended)
```python
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 🔑 Setup

### 1. Create a .env file in the project root:

```env
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
TWILIO_NUMBER=+1234567890
RECEIVER_NUMBER=+919876543210
```

### 2. Download YOLOv12x weights:
- Ensure yolo12x.pt is present in your project directory.

Update in code:
```python
from ultralytics import YOLO
model = YOLO("yolo12x.pt")
```

### 3. ▶️ Usage
- Run the detection script:

```bash
python main.py
```

- Press Q to exit the webcam feed.

- When an animal is detected, an SMS alert will be sent to your registered number.

### 4. 📊 Model Confidence
- model.conf sets the detection confidence threshold.
- Recommended: 0.5 – 0.6

- Lower → more detections, but may include false positives.
- Higher → fewer detections, but more accurate.

```python
model.conf = 0.5  # Balanced default
```

## 🛠️ Future Improvements
- Add email or WhatsApp alerts.
- Deploy on Raspberry Pi devices.
- Save detection frames or video logs.

## 📜 License
This project is licensed under the MIT License.
