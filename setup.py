import pkg_resources
from setuptools import setup
from setuptools import find_packages

def pillow_installed():
    """Check if Pillow is installed"""
    pillow_req = pkg_resources.Requirement.parse('Pillow')
    try:
        pkg_resources.get_provider(pillow_req)
    except pkg_resources.DistributionNotFound:
        return False
    else:
        return True

install_requires = ['setuptools', 'CherryPy']

if pillow_installed():
    install_requires.append('Pillow')
else:
    install_requires.append('PIL')

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

    install_requires = install_requires,

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
