import cv2
import numpy as np
import socket

# Adresse IP et port de réception du flux vidéo
IP_RECEIVE = '0.0.0.0'
PORT_RECEIVE = 5000

# Initialise le socket pour recevoir le flux vidéo
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP_RECEIVE, PORT_RECEIVE))

# Initialise le codec vidéo
fourcc = cv2.VideoWriter_fourcc(*'H264')

while True:
    # Réception des données du flux vidéo encodé via le socket
    data, addr = sock.recvfrom(65507)
    data = np.frombuffer(data, dtype=np.uint8)

    # Décodage de l'image avec le codec vidéo
    frame = cv2.imdecode(data, cv2.IMREAD_COLOR)



    # Affichage de l'image
    cv2.imshow('Video', frame)
    cv2.waitKey(1)
