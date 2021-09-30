import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name="pytento",
  version="1.0.8",
  author="Demir Antay",
  author_email="demir99antay@gmail.com",
  description='This is a staticly-typed testing framework',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/demirantay/pytento',
  packages=setuptools.find_packages(),
  license='MIT',
)
