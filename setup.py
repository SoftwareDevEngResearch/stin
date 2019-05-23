import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / 'README.md').read_text()
CHANGELOG = (HERE / 'CHANGELOG.md').read_text()
ldisc = README + '\n\n' + CHANGELOG

VERSION = (HERE / '_version.py').read_text()
exec(VERSION)

setup(
    name="stin",
    version=__version__,
    description="Simulates steady influx of air into water",
    long_description=ldisc,
    long_description_content_type="text/markdown",
    url="https://github.com/SoftwareDevEngResearch/stin",
    author="Ivan Nepomnyashchikh",
    author_email="nepomnyi@oregonstate.edu",
    license="MIT",
    python_requires='>=3',
    install_requires=['numpy', 'matplotlib', 'pyyaml'],
    tests_require=['pytest==3.6', 'pytest-cov'],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Natural Language :: English',
        'Intended Audience :: Engineering/Research'
    ],
    packages=['stin', 'stin.tests'],
    include_package_data=True,
)
