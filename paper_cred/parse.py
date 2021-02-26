import pyzbar.pyzbar as pzybar


def parse_uri(uri):
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


def parse_qr(image):
    return parse_uri(str(pzybar.decode(image)[0].data, "UTF-8"))
