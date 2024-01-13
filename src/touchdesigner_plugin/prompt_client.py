import socket
import struct

import cv2
import numpy as np

from touchdesigner_plugin.constants import HOST, PORT


class PromptClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))
        self.image = None

    def run(self, prompt: str):
        try:
            # Send prompt to server
            self.client_socket.send(prompt.encode())

            # Receive image from server
            self.receive_image()

            # print("Image received successfully")
        except Exception as e:
            print(f"Exception: {e}")

    def receive_image(self):
        image_size_data = self.client_socket.recv(4)

        # Unpack the image size as a 4-byte integer
        image_size = struct.unpack("!I", image_size_data)[0]

        # Receive image data
        image_data = b""
        while len(image_data) < image_size:
            chunk = self.client_socket.recv(min(image_size - len(image_data), 4096))
            if not chunk:
                break
            image_data += chunk

        # Decode the image data using cv2.imdecode
        self.image = cv2.imdecode(
            np.frombuffer(image_data, dtype=np.uint8), cv2.IMREAD_COLOR
        )

        # Save the received image
        cv2.imwrite("received_image.jpg", self.image)

    def __del__(self) -> None:
        self.client_socket.close()


if __name__ == "__main__":
    prompt_client = PromptClient()
    prompt_client.run("Test prompt!!")
