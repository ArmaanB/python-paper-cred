import pyzbar.pyzbar as pzybar


def decode(image):
    return str(pzybar.decode(image)[0].data, "UTF-8")
