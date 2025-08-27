from dotenv import load_dotenv
import os
load_dotenv('.env')

import cv2
import torch
from twilio.rest import Client

from ultralytics import YOLO

model = YOLO("yolo12x.pt")
model.conf = 0.5


animal_keywords = [
    'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe',
    'bird', 'deer', 'fox', 'rabbit', 'monkey',
    'goat', 'duck', 'pig', 'hen', 'chicken'
]

account_sid: str= os.getenv('ACCOUNT_SID')
auth_token: str= os.getenv('AUTH_TOKEN')
twilio_number: str= os.getenv('TWILIO_NUMBER')
receiver_number: str= os.getenv('RECEIVER_NUMBER')


client = Client(account_sid, auth_token)

cap = cv2.VideoCapture(0)
sent_labels = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)  
    detections = results[0].boxes  

    for box in detections:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int) 
        conf = float(box.conf[0])  
        cls = int(box.cls[0])     
        label = model.names[cls]

        if any(animal in label.lower() for animal in animal_keywords):
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            if label not in sent_labels:
                print(f"{label} detected!")
                try:
                    message = client.messages.create(
                        body=f"{label.capitalize()} detected near the system!",
                        from_=twilio_number,
                        to=receiver_number
                    )
                    print(f"SMS sent: {message.sid}")
                    sent_labels.add(label)
                except Exception as e:
                    print("Error sending SMS:", e)


    cv2.imshow("Animal Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()