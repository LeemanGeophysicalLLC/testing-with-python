"""Setup script for installing meteogram."""

from setuptools import find_packages, setup


setup(
    name='meteogram',
    version=0.1,
    description='Collection of tools for reading, visualizing and'
                'performing calculations with weather data.',
    long_description='The space MetPy aims for is GEMPAK '
                     '(and maybe NCL)-like functionality, in a way that '
                     'plugs easily into the existing scientific Python '
                     'ecosystem (numpy, scipy, matplotlib).',

    url='http://github.com/Unidata/MetPy',

    author='John Leeman',
    author_email='john@leemangeophysical.com',
    maintainer='John Leeman',
    maintainer_email='john@leemangeophysical.com',

    license='BSD',

    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Atmospheric Science',
                 'Intended Audience :: Science/Research',
                 'Operating System :: OS Independent',
                 'License :: OSI Approved :: BSD License'],
    keywords='meteorology weather',

    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
    install_requires=['matplotlib>=2.2.0', 'numpy>=1.12.0', 'pandas>=0.24.2'],
    extras_require={
        'test': ['pytest>=2.4', 'pytest-runner', 'pytest-mpl', 'pytest-flake8']
    },


    zip_safe=True)
