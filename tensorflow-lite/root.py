"""
Run object detection on images, Press ESC to exit the program
For Raspberry PI, please use `import tflite_runtime.interpreter as tflite` instead
"""
import re
import cv2
import numpy as np

import tflite_runtime.interpreter as tflite

import igeCore as core
from igeCore.apputil import graphicsHelper

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
CAMERA_TEXTURE_SIZE = 512

def load_labels(label_path):
    r"""Returns a list of labels"""
    with open(label_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def load_model(model_path):
    r"""Load TFLite model, returns a Interpreter instance."""
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

def process_image(interpreter, image, input_index, k=3):
    r"""Process an image, Return top K result in a list of 2-Tuple(confidence_score, _id)"""
    input_data = np.expand_dims(image, axis=0)  # expand to 4-dim

    # Process
    interpreter.set_tensor(input_index, input_data)
    interpreter.invoke()

    # Get outputs
    output_details = interpreter.get_output_details()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    # print(output_data.shape)  # (1, 1001)
    output_data = np.squeeze(output_data)

    # Get top K result
    top_k = output_data.argsort()[-k:][::-1]  # Top_k index
    result = []
    for _id in top_k:
        score = float(output_data[_id] / 255.0)
        result.append((_id, score))

    return result


def display_result(top_result, frame, labels):
    r"""Display top K result in top right corner"""
    for idx, (_id, score) in enumerate(top_result):
        # print('{} - {:0.4f}'.format(label, score))
        x = 72
        y = 72 + 24 * idx
        cv2.putText(frame, '{} - {:0.4f}'.format(labels[_id], score), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    cam_texture.setImage(cv2.resize(cv2.cvtColor(cv2.flip(frame, 0), cv2.COLOR_BGR2RGB), (CAMERA_TEXTURE_SIZE, CAMERA_TEXTURE_SIZE)))

if __name__ == "__main__":
    model_path = 'mobilenet_v1_1.0_224_quant.tflite'
    label_path = 'mobilenet_v1_1.0_224_labels.txt'

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, 30)

    core.window(True, CAMERA_WIDTH, CAMERA_HEIGHT)
    cam_texture = core.texture("camera", CAMERA_TEXTURE_SIZE, CAMERA_TEXTURE_SIZE, format=core.GL_RGB)
    cam_sprite = graphicsHelper.createSprite(CAMERA_WIDTH, CAMERA_HEIGHT, cam_texture)

    camera = core.camera("cam01")
    camera.orthographicProjection = True
    camera.position = (0, 0, 100)

    showcase = core.showcase("showcase01")
    showcase.add(cam_sprite)

    interpreter = load_model(model_path)
    labels = load_labels(label_path)

    input_details = interpreter.get_input_details()

    # Get Width and Height
    input_shape = input_details[0]['shape']
    height = input_shape[1]
    width = input_shape[2]

    # Get input index
    input_index = input_details[0]['index']

    # Process Stream
    while True:
        core.update()
        ret, frame = cap.read()
        if frame is not None:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (width, height))
            top_result = process_image(interpreter, image, input_index)
            display_result(top_result, frame, labels)

        # render the objects contained in showcase from the camera.
        camera.shoot(showcase)

        # update frame buffer
        core.swap()
    cap.release()
