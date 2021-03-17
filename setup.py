
from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='bookpam',
    version='0.0.1',
    description='BookPam is a typesetting system; it includes features designed for the production of technical documentation and book.',
    long_description=open('README.txt').read() + '\n\n' +
    open('CHANGELOG.txt').read(),
    url='https://maxbase.org/',
    author='Max Base',
    author_email='maxbasecode@gmail.com',
    license='GNU GENERAL PUBLIC LICENSE',
    classifiers=classifiers,
    keywords='bookpam',
    packages=find_packages(),
    install_requires=['']
)
