from setuptools import setup, find_packages

DISTNAME = 'iSeaborn'
MAINTAINER = 'Golam Mostaeen'
MAINTAINER_EMAIL = 'golammostaeen@gmail.com'
URL = 'https://iseaborn.readthedocs.io/en/latest/'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/pseudoPixels/iSeaborn'
VERSION = '0.0.1.dev'

INSTALL_REQUIRES = [
      'pandas',
      'bokeh==1.4.0',
      'numpy',
      'seaborn'
]

PACKAGES = [
    'iSeaborn',
    'iSeaborn.colors',
    'iSeaborn.external',
    'iSeaborn.tests',
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: BSD License',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Multimedia :: Graphics',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS'
]





setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        # description=DESCRIPTION,
        # long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        include_package_data=True,
        install_requires=INSTALL_REQUIRES,
        packages=find_packages(),
        classifiers=CLASSIFIERS
    )