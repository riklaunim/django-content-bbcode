from os import path
from setuptools import setup, find_packages


def read(name):
    return open(path.join(path.dirname(__file__), name)).read()

setup(
    name='django-content-bbcode',
    version='0.0.2',
    description='Advanced BBCode alike tags parser',
    long_description=read('README.md'),
    author='Piotr Malinski',
    author_email='riklaunim@gmail.com',
    url='https://github.com/riklaunim/django-content-bbcode',
    packages=find_packages(exclude=["content_bbcode_demo"]),
    install_requires=[
        'Django',
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
