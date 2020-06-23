import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hocon",
    use_scm_version=True,
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
    install_requires=['pyhocon>=0.3.55'],
    setup_requires=['setuptools_scm', "wheel"],
    extras_require={
        "dev": ["mypy", "pytest", 'pylint', "twine", "bump2version"],
    },
)

