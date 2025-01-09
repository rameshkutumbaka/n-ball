from setuptools import setup, find_packages

setup(
    name="n-ball",  # Name of the package
    version="0.1.0",  # Version of the package
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[],  # Add any dependencies here
    description="Gen AI Projects...",
    author="rameshkutumbaka",
    author_email="rameshkutumbaka@gmail.com",
    url="https://github.com/rameshkutumbaka/n-ball",  # URL of the repository
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the required Python version
)
