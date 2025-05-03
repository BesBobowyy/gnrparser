from setuptools import setup, find_packages

setup(
    name="gnrparser",
    version="1.0.0",
    description="A lightweight library for parsing .gnr files and operating on structured game data.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="BesBobowyy",
    author_email="",
    url="https://github.com/BesBobowyy/gnrparser",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.6',
)