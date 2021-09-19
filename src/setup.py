import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="market_list",  # Replace with your own username
    version="0.0.1",
    author="Jorge Rivero",
    author_email="jorvivero83@gmail.com",
    description="This is project to generate the market list based on a kitchen recipes list.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jorivero83/market_list",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy>=1.14.3",
        "pandas>=0.23.0",
        "psycopg2>=2.8.4"
    ],
)