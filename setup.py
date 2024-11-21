from setuptools import setup, find_packages

setup(
    name="jay-bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'blinker>=1.9.0',
        'Flask>=3.1.0',
        'gunicorn>=23.0.0',
        'python-dotenv>=1.0.1',
        'requests>=2.32.3',
    ],
    author="Jay Trevino",
    description="A fine-tuned language model representing Jay.",
    url="https://github.com/jat2211/jay-bot",
)