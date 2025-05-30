import cv2
import torch
from twilio.rest import Client

model = torch.hub.load('ultralytics/yolov5', 'yolov5l', trust_repo=True)
model.conf = 0.5


animal_keywords = [
    'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe',
    'bird', 'deer', 'fox', 'rabbit', 'monkey',
    'goat', 'duck', 'pig', 'hen', 'chicken'
]


#Uncomment the code block below and enter your Twilio credentials
'''

account_sid = 'ABC'
auth_token = 'xyz'
twilio_number = '+1234'
receiver_number = '+910000'
client = Client(account_sid, auth_token)

'''
cap = cv2.VideoCapture(0)
sent_labels = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    detections = results.xyxy[0]

    for *box, conf, cls in detections:
        label = model.names[int(cls)]
        if any(animal in label.lower() for animal in animal_keywords):
            cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(
                box[2]), int(box[3])), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(box[0]), int(
                box[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

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
