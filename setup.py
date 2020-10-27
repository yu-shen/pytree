import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytree",
    version="0.0.1",
    author="Shen Yu",
    author_email="yu.shen@me.com",
    description="Python implementation of a self-balancing binary search tree",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yu-shen/pytree",
    packages=setuptools.find_packages(),
    tests_require=['pytest'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
