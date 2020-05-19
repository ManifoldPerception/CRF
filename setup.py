import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CRF",
    version="0.0.1a1",
    author="Manifold Perception",
    author_email="khue@manifoldperception.com",
    description="Conditional Random Fields for Vision and Language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ManifoldPerception/CRF",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
