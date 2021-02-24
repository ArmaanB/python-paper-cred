from setuptools import setup
import os

pwd = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(pwd, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="paper_cred",
    version="0.0.0",
    description="PathCheck Verifiable Vaccination Credentials implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pathcheck.org",
    author="PathCheck foundation",
    license="MIT",
    packages=["paper_cred"],
    install_requires=["pyzbar", "Pillow"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha"
        "License :: OSI Approved :: MIT License",
    ],
)
