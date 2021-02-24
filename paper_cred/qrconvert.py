from pyzbar.pyzbar import decode


def qrconvert(image):
    return decode(image)[0].data.decode()
