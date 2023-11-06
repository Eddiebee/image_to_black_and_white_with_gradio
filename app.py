import gradio as gr 
import numpy as np


def black_and_white(input_img):
    black_and_white_img = np.dot(input_img[...,:3], [0.2989, 0.5870, 0.1140])
    black_and_white_img /= black_and_white_img.max()
    return black_and_white_img


demo = gr.Interface(black_and_white, gr.Image(label="Original Image"), gr.Image(label="Black and White Image", image_mode="L"))
demo.launch()