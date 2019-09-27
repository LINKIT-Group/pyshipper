import os
import setuptools

envstring = lambda var: os.environ.get(var) or ""

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=envstring("NAME"),
    version=envstring("VERSION"),
    author=envstring("AUTHOR"),
    author_email=envstring("AUTHOR_EMAIL"),
    description=envstring("DESCRIPTION"),
    url=envstring("URL"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[envstring("NAME"), envstring("NAME") + ".main"],
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
