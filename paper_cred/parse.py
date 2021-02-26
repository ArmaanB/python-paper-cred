import ecdsa
import pyzbar.pyzbar as pzybar


def verify_sig(data):
    vk = ecdsa.VerifyingKey.from_pem(open("./examples/public.key").read())
    print(data["signature"])
    print(data["payload"])
    return vk.verify(
        bytes(data["signature"], "utf-8"),
        bytes(data["payload"], "utf-8"),
    )


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

    if verify_sig(outp):
        return outp
    else:
        return False


def parse_qr(image):
    return parse_uri(str(pzybar.decode(image)[0].data, "UTF-8"))
