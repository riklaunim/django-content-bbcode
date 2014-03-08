from setuptools import setup, find_packages


setup(
    name='django-content-bbcode',
    version='0.0.1',
    description='Advanced BBCode alike tags parser',
    long_description=open('README.rst', 'r').read(),
    author='Piotr Malinski',
    author_email='riklaunim@gmail.com',
    url='https://github.com/riklaunim/django-content-bbcode',
    packages=find_packages(exclude=["*.demo"]),
    install_requires=[
        'Django',
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)