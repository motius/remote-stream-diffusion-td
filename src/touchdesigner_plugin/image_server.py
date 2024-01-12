import socket
import cv2 as cv
import struct

from touchdesigner_plugin.constants import HOST, PORT, JPEG_ENCODE_QUALITY_PERCENT


class ImageServer:
    def __init__(self, use_webcam: int = 0):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(3)

        self.use_webcam = use_webcam
        if self.use_webcam:
            self.cap = cv.VideoCapture(use_webcam)
        else:
            self.image_path = "imgs/IMG_7418_1280x720.jpg"

        print(f"Server listening on {HOST}:{PORT}")

    def send_image(self, client_socket):
        # ToDo generate image here
        if not self.use_webcam:
            image = cv.imread(self.image_path)
        else:
            ret, image = capture.read()

        # NOTE: decrease JPEG_ENCODE_QUALITY_PERCENT to increase performance
        _, image_data = cv.imencode(
            '.jpg', image, [int(cv.IMWRITE_JPEG_QUALITY), JPEG_ENCODE_QUALITY_PERCENT]
        )

        image_size = struct.pack("!I", len(image_data))
        client_socket.send(image_size)
        client_socket.send(image_data.tobytes())

    def run(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")

            try:
                # Receive prompt from client
                prompt = client_socket.recv(2048).decode()
                print(f"Received prompt: {prompt}")

                # Send image to client
                self.send_image(client_socket)

                print("Image sent successfully")
            except Exception as e:
                print(f"Exception: {e}")
            finally:
                client_socket.close()

    def __del__(self):
        print("Closing server socket..")
        self.server_socket.close()


if __name__ == "__main__":
    image_server = ImageServer()
    image_server.run()
