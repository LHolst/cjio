from setuptools import setup
from pathlib import Path
import cjio

CURRENT_DIR = Path(__file__).parent

# Package meta-data.
NAME = 'cjio'
DESCRIPTION = 'CLI to process and manipulate CityJSON files.'
URL = 'https://github.com/tudelft3d/cjio'
EMAIL = 'h.ledoux@tudelft.nl, b.dukai@tudelft.nl'
AUTHOR = 'Hugo Ledoux, Balázs Dukai'
REQUIRES_PYTHON = '>=3.5.0'

# What packages are required for this module to be executed?
REQUIRED = [
    'Click',
    'jsonschema',
    'jsonref'
]

# What packages are optional?
EXTRAS = {
    'export': ['mapbox-earcut', 'numpy'],
    'reproject': ['pyproj'],
    'api': ['pandas']
}

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=cjio.__version__,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=['cjio'],
    package_data={'cjio': ['schemas/0.9/*', 'schemas/1.0.0/*', 'schemas/1.0.1/*']},
    # include_package_data=True,
    license = 'MIT',
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: GIS',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows'
    ],
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    entry_points='''
        [console_scripts]
        cjio=cjio.cjio:cli
    ''',
)
