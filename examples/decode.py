#!/usr/bin/env python3

import sys
from PIL import Image
from paper_cred import qrconvert


def main():
    if len(sys.argv) <= 1:
        sys.exit(
            "Please provide a path to the QR code. Examples are in the "
            "examples/qr directory."
        )
    return qrconvert.decode(Image.open(sys.argv[1]))


if __name__ == "__main__":
    print(main())
