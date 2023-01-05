from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tvscrape",
    version="2.1.0",
    packages=["tvScrape"],
    url="https://github.com/stevenmichiels/tvscrape/",
    license="MIT License",
    author="@stevenmichiels",
    author_email="",
    description="TradingView historical data downloader",
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=[
        "setuptools",
        "pandas",
        "websocket-client",
        "requests"
    ],
)
