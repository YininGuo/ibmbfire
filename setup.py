# setup.py
from setuptools import setup, find_packages

setup(
    name='ibmbfire',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    author='Yining_Guo',
    author_email='yining.guo.23@ucl.ac.uk',
    description='Generate IBMB fire temperature-time curves from compartment geometry and other parameters',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ibmbfire',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
