from setuptools import setup, find_packages
from setuptools.command.install import install

class f(install):
    pass

setup(
    name='pydockerd',
    version='0.0.1',
    description='dockerd but python, on linux, osx, windows, arm, freebsd, solaris',
    author='du7ec',
    author_email='dutec6834@gmail.com',
    url='https://github.com/FarAway6834/pydockerd',
    packages=find_packages(exclude=[])
    include_package_data=True,
    package_data={
        "mydockerd": ["__main__.pyz"]
    },
    keywords=['dockerd', 'docker', 'pydocker', 'pydockerd'],
    python_requires='>=3.4',
    package_data={},
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: UNIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Solaris"
    ],
)