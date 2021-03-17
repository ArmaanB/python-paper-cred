#!/usr/bin/env python3
"""
Take a path to a QR code image as input, and print the decoded content.
Requires Pillow.
"""

from paper_cred import parse


def main():
    inp = {
        "type": "COUPON",
        "version": "1",
        "signature": "48JK2ZH25J7Z03WZHAB4JPUJ3P03LHR4HHUU71OAGWTACQ4KGK4B9XCNKJKY0IML6P2QFJU2GOI9EM4B6YHZJIMXLDV5EVNNCNQL8F6XFBPQI9DR",
        "pubkey": "PCF.VITORPAMPLONA.COM",
        "payload": "1/5000/SOMERVILLE%20MA%20US/1A/%3E65",
    }
    return parse.encode_uri(inp)


if __name__ == "__main__":
    print(main())
