import glob
import socket
import struct
import os
import sys
from typing import Literal, Dict, Optional

import cv2 as cv
import numpy as np

from touchdesigner_plugin.constants import HOST, JPEG_ENCODE_QUALITY_PERCENT, PORT
from touchdesigner_plugin.utilities import get_random_image

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from utils.wrapper import StreamDiffusionWrapper

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class StreamDiffusionServer:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(5)

        model_id_or_path: str = "KBlueLeaf/kohaku-v2.1"
        lora_dict: Optional[Dict[str, float]] = None
        width: int = 512
        height: int = 512
        acceleration: Literal["none", "xformers", "tensorrt"] = "xformers"
        use_denoising_batch: bool = False
        seed: int = 2

        self.stream = StreamDiffusionWrapper(
            model_id_or_path=model_id_or_path,
            lora_dict=lora_dict,
            t_index_list=[0, 16, 32, 45],
            frame_buffer_size=1,
            width=width,
            height=height,
            warmup=10,
            acceleration=acceleration,
            mode="txt2img",
            use_denoising_batch=use_denoising_batch,
            cfg_type="none",
            seed=seed,
        )

        print(f"Server listening on {HOST}:{PORT}")

    def send_image(self, client_socket):
        # ToDo generate image here
        # image = get_random_image(nb_circles=3, noise_background=False)
        image = np.array(self.stream())


        # NOTE: decrease JPEG_ENCODE_QUALITY_PERCENT to increase performance
        _, image_data = cv.imencode(
            ".jpg", image, [int(cv.IMWRITE_JPEG_QUALITY), JPEG_ENCODE_QUALITY_PERCENT]
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

                self.stream.prepare(
                    prompt=prompt,
                    num_inference_steps=50,
                )
                
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
    stream_diffusion_server = StreamDiffusionServer()
    stream_diffusion_server.run()
