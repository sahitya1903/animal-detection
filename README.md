# 🐾 Animal Detection Alert System

A real-time **animal detection system** using **YOLOv12x**, **OpenCV**, and **Twilio SMS API**.  
It detects animals from a webcam feed and sends an **SMS alert** when an animal is spotted.  

---

## 🚀 Features
- Real-time video stream analysis with **YOLOv12x**.
- Detects animals like **cats, dogs, cows, elephants, birds, etc.**.
- **Sends SMS alerts** via Twilio only once per detected animal to avoid spam.
- Live bounding boxes drawn on detected animals.

---

## 📂 Project Structure
.
├── main.py # Core detection script
├── .env # Environment variables (Twilio credentials & phone numbers)
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/yourusername/animal-detection-alert.git
cd animal-detection-alert

2. Create a virtual environment (optional but recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
requirements.txt should include:

Copy code
opencv-python
torch
ultralytics
twilio
python-dotenv
🔑 Setup
Create a .env file in the project root:

env
Copy code
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
TWILIO_NUMBER=+1234567890
RECEIVER_NUMBER=+919876543210
Download YOLOv12x weights:
Make sure yolo12x.pt is in your project folder.

In your script:

python
Copy code
from ultralytics import YOLO
model = YOLO("yolo12x.pt")
▶️ Usage
Run the detection script:

bash
Copy code
python main.py
Press Q to exit the live feed.

When an animal is detected, you’ll receive an SMS alert.

📊 Model Confidence
model.conf is the detection confidence threshold.

Recommended value: 0.5–0.6

Lower → more detections but risk of false alarms.

Higher → fewer detections but more accurate.

python
Copy code
model.conf = 0.5  # Default balanced value
📸 Demo
(You can add screenshots or GIFs of bounding boxes around animals here)

🛠️ Future Improvements
Add email or WhatsApp alerts.

Deploy on Raspberry Pi for outdoor use.

Save detected frames for later review.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License
MIT

