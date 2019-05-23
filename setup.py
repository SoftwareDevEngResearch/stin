import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="stin",
    version="0.1.0",
    description="Simulates steady influx of air into water",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SoftwareDevEngResearch/stin",
    author="Ivan Nepomnyashchikh",
    author_email="nepomnyi@oregonstate.edu",
    license="MIT",
    python_requires='>=3',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Intended Audience :: Engineering/Research'
    ],
    packages=['stin', 'stin.tests'],
    include_package_data=True,
    install_requires=['numpy', 'matplotlib', 'pyyaml'],
)
