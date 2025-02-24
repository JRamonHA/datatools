from setuptools import setup, find_packages

setup(
    name='datatools',
    version='0.0.1'
    author=['José Ramón Hernández'],
    author_email=['jrha@ier.unam.mx'],
    url='https://github.com/JRamonHA/datatools',
    license='MIT',
    packages=['datatools'],
    packages=find_packages(),
    install_requires=['pandas'],
)
