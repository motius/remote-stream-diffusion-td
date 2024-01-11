import socket
import time
import cv2

HOST = ""
PORT = 1234

capture = cv2.VideoCapture(0)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

for i in range(0,15):
    ret, frame = capture.read()
    data = cv2.imencode('.jpg', frame)[1].tostring()
    sock.sendall(data)
    time.sleep(1)

sock.close()
