import socket
import cv2
import numpy as np

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]


def send_image(client_socket, image_path):
    # Read image
    image = cv2.imread(image_path)

    print(f"Sending {image_path} of original size {image.shape} which is {image.shape[0] * image.shape[1] * image.shape[2]}")

    # Convert image to bytes
    _, image_data = cv2.imencode('.jpg', image)
    print(f"after encoding {image_data.shape=}")
    image_bytes = image_data.tobytes()

    # Send image size to client
    client_socket.send(str(len(image_bytes)).encode())

    # Send image data to client
    client_socket.send(image_bytes)


def main():
    # Server configuration
    host = '127.0.0.1'
    port = 12345

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(3)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            # Receive prompt from client
            prompt = client_socket.recv(2048).decode()
            print(f"Received prompt: {prompt}")

            # Send image to client
            send_image(
                client_socket, "imgs/IMG_7418_1280x720.jpg"
            )

            print("Image sent successfully")
        finally:
            client_socket.close()


if __name__ == "__main__":
    main()
