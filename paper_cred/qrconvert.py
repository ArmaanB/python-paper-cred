from pyzbar.pyzbar import decode
import json


def decode(image):
    return json.load(decode(image)[0])
