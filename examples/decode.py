from PIL import Image
from paper_cred import qrconvert


def main():
    return qrconvert.decode(Image.open("qr.png"))


if __name__ == "__main__":
    print(main())
