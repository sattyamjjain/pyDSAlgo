from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="PyDSAlgo",
    version="1.1.0",
    author="Sattyam Jain",
    author_email="sattyamjain96@gmail.com",
    description="Python Package for Data structure and algorithms implementation with its proper explanation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sattyamjjain/pyDSAlgo",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=[
        "pydsa",
        "pydsalgo"
        "dsa",
        "data structure",
        "algo",
        "algorithm",
        "ds",
        "python data structure",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    project_urls={
        "Bug Reports": "https://github.com/sattyamjjain/pyDSAlgo",
        "Source": "https://github.com/sattyamjjain/pyDSAlgo",
    },
)
