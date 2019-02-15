from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lambdata-brit228',
    version='0.0.11',
    description='Pandas DataFrame helper utilities.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/brit228/DS1-Unit3-Sprint1-Module1',
    author='Michael Beck',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='pandas helper utilities',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    python_requires='>=3, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',

    install_requires=['pandas', 'scipy', 'numpy'],

    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    # data_files=[('my_data', ['data/data_file'])],

    # entry_points={  # Optional
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },

    project_urls={
        'Bug Reports': 'https://github.com/brit228/DS1-Unit3-Sprint1-Module1'
    },
)
