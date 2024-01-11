import socket
import cv2
import numpy as np

from touchdesigner_plugin.constants import IMG_WIDTH, IMG_HEIGHT, RGB_CHANNELS


def receive_image(server_socket):
    # Receive image size
    image_size = int(server_socket.recv(391049).decode())

    print(f"Received image size: {image_size}")
    # Receive image data
    image_data = server_socket.recv(image_size)

    print(f"len of received image_data: {len(image_data)}")

    # Convert bytes to numpy array
    image_array = np.frombuffer(image_data, dtype=np.uint16)
    print(f"{image_array.shape=}")

    # Decode image
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    # image = image_array.reshape((IMG_HEIGHT, IMG_WIDTH, RGB_CHANNELS))


    # Save the received image
    cv2.imwrite("received_image.jpg", image)


def main():
    # Client configuration
    host = '127.0.0.1'
    port = 12345

    # Prompt to send to the server
    prompt = "Send me an image!"

    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

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
