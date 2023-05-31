from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='APIrate',
    url='https://github.com/Kumariz0/APIrate',
    author='Jodokus Heck',
    author_email='jodokus.heck@gmail.com',
    # Needed to actually package something
    packages=['APIrate'],
    # Needed for dependencies
    install_requires=['requests'],
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.md').read(),
)