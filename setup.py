from setuptools import setup
from setuptools import find_packages

setup(
    name="dowser",

    packages=find_packages('src'),

    license = 'PSF',
    description = """Debugging Python’s Memory Usage with Dowser""",
    long_description = """Debugging Python’s Memory Usage with Dowser""",

    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    install_requires = ['PIL', 'setuptools', 'CherryPy'],

    package_dir = {'': 'src'},
    package_data = {'': [
        'tree.html',
        'trace.html',
        'main.css',
        'graphs.html',
    ]},
    include_package_data = True,
    zip_safe = False,

    entry_points = dict(
        console_scripts = ['dowser = dowser:main'],
        gui_scripts = [],
    ),
)
