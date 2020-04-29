import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hocon",
    version="0.0.2",
    author="Daniel Braun",
    author_email="danie.braun@outlook.co.il",
    description="HOCON encoder and decoder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danielbraun89/hocon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pyhocon>=0.3.54'],  # Optional
)

