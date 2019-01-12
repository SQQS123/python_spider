from captcha.image import ImageCaptcha
from PIL import Image
import numpy as np


# 先定义一个词表和其长度变量
VOCAB = ['0','1','2','3','4','5','6','7','8','9']
CAPTCHA_LENGTH = 4
VOCAB_LENGTH = len(VOCAB)

def text2vec(text):
    if len(text) > CAPTCHA_LENGTH:
        return False
    vector = np.zeros(CAPTCHA_LENGTH * VOCAB_LENGTH)
    for i, c in enumerate(text):
        index = i * VOCAB_LENGTH + VOCAB.index(c)
        vector[index] = 1
    return vector


def vec2text(vector):
    if not isinstance(vector,np.ndarray):
        vector = np.asarray(vector)
    vector = np.reshape(vector, [CAPTCHA_LENGTH, -1])
    text = ''
    for item in vector:
        text += VOCAB[np.argmax(item)]
    return text


def generate_captcha(captcha_text):
    image = ImageCaptcha()
    captcha = image.generate(captcha_text)
    captcha_image = Image.open(captcha)
    captcha_array = np.array(captcha_image)
    return captcha_array


# captcha = generate_captcha('1234')
# print(captcha,captcha.shape)
vector = text2vec('1234')
text = vec2text(vector)
print(vector, text)

