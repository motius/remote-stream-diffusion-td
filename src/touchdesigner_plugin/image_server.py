import socket
import cv2 as cv
import struct

from touchdesigner_plugin.constants import HOST, PORT, JPEG_ENCODE_QUALITY_PERCENT


def send_image(client_socket, image_path):
    # ToDo generate image here
    image = cv.imread(image_path)

    # NOTE: decrease JPEG_ENCODE_QUALITY_PERCENT to increase performance
    _, image_data = cv.imencode(
        '.jpg', image, [int(cv.IMWRITE_JPEG_QUALITY), JPEG_ENCODE_QUALITY_PERCENT]
    )

    image_size = struct.pack("!I", len(image_data))
    client_socket.send(image_size)
    client_socket.send(image_data.tobytes())


def main():
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(3)

    print(f"Server listening on {HOST}:{PORT}")

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
