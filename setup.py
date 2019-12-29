from setuptools import setup, find_packages

NAME="gPhoto-object-extraction"
__version__ = '1.0.0'
AUTHOR="Guillain"
AUTHOR_EMAIL="guillain@gmail.com"

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name=NAME,
    version=__version__,
    description="Image analysis with IA",
    url='https://gitlab.com/bo-art-of-bonsai/' + NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license='Private',
    install_requires=requirements,
    packages=find_packages(),
    zip_safe=False
)
