import cv2
import numpy as np
import socket

# Adresse IP et port de destination du flux vidéo
IP_DESTINATION = '0.0.0.0'
PORT_DESTINATION = 5000

# Ouvre la webcam
cap = cv2.VideoCapture(0)

# Initialise le socket pour envoyer le flux vidéo
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Initialise le codec vidéo
fourcc = cv2.VideoWriter_fourcc(*'H264')

while True:
    # Capture une image à partir de la webcam
    ret, frame = cap.read()

    # Encode l'image avec le codec vidéo
    encoded, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
    data = np.array(buffer)

    # Envoie les données du flux vidéo encodé via le socket
    sock.sendto(data, (IP_DESTINATION, PORT_DESTINATION))
