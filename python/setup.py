import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hopper_api",
    version="0.3.0",
    author="The hopper team",
    author_email="info@hoppercloud.net",
    description="Hopper's app API",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/hopper-team/hopper-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyjwt',
        'pyjwt[crypto]'
    ],
    python_requires='>=3.6',
)
