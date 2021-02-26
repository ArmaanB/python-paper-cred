#!/usr/bin/env python3

import sys
from PIL import Image
from paper_cred import parse


def main():
    if len(sys.argv) <= 1:
        sys.exit(
            "Please provide a path to the QR code. Examples are in the "
            "examples/qr directory."
        )
    return parse.parse_qr(Image.open(sys.argv[1]))


if __name__ == "__main__":
    print(main())
