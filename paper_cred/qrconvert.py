import pyzbar.pyzbar as pzybar


def decode(image):
    return pzybar.decode(image)[0].data
