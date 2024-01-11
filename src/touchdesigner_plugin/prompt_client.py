import socket
import cv2
import numpy as np
import struct

from touchdesigner_plugin.constants import PORT, HOST


def receive_image(server_socket):
    # Receive the 4-byte image size
    image_size_data = server_socket.recv(4)

    # Unpack the image size as a 4-byte integer
    image_size = struct.unpack("!I", image_size_data)[0]

    # Receive image data
    image_data = b""
    while len(image_data) < image_size:
        chunk = server_socket.recv(min(image_size - len(image_data), 4096))
        if not chunk:
            break
        image_data += chunk

    # Decode the image data using cv2.imdecode
    image = cv2.imdecode(np.frombuffer(image_data, dtype=np.uint8), cv2.IMREAD_COLOR)

    # Save the received image
    cv2.imwrite("received_image.jpg", image)


def main():

    # Prompt to send to the server
    prompt = "Send me an image!"

    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    try:
        # Send prompt to server
        client_socket.send(prompt.encode())

        # Receive image from server
        receive_image(client_socket)

        print("Image received successfully")
    finally:
        client_socket.close()


if __name__ == "__main__":
    main()
