import pyzbar.pyzbar as pzybar


def decode_uri(uri):
    """
    Method to parse URI

    Parameters
    ----------
    uri : str
        Input URI.

    Returns
    -------
    dict
        A dict of the data parsed from the URI. Contains type, version,
        signature, pubkey, and payload.

    """
    colon = uri.split(":", 4)
    question = colon[3].split(".", 1)[1].split("?")
    outp = {
        "type": colon[1],
        "version": colon[2],
        "signature": colon[3].split(".")[0],
        "pubkey": question[0],
        "payload": question[1:][0],
    }

    return outp


def encode_uri(inp):
    """
    Method to create URI

    Parameters
    ----------
    inp : dict
        A dict with type, version, signature, pubkey, and payload.

    Returns
    -------
    str
        A string of the input in URI format.

    """
    typ = inp["type"]
    ver = inp["version"]
    sig = inp["signature"]
    pub = inp["pubkey"]
    pay = inp["payload"]
    return f"cred:{typ}:{ver}:{sig}:{pub}:{pay}"


def parse_qr(image):
    """
    Method to parse QR code using pyzbar

    Parameters
    ----------
    image : PIL.Image, numpy.ndarray
        Input image.

    Returns
    -------
    dict
        A dict of the data parsed from the QR code. Contains type, version,
        signature, pubkey, and payload.

    """
    return decode_uri(str(pzybar.decode(image)[0].data, "UTF-8"))
