from setuptools import find_packages, setup

setup(
    name="deal",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "deal = deal.main:main",
        ],
    },
)
