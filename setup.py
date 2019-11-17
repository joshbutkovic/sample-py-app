from setuptools import setup, find_packages


with open('README.md') as file:
    readme = file.read()

setup(
    name='myapp',
    version='0.1.0',
    description='An example structure for simple apps',
    long_description=readme,
    author='Josh Butkovic',
    author_email='joshbutkovic@gmail.com',
    url='https://github.com/joshbutkovic/sample-py-app',
    packages=find_packages(exclude=('tests', 'dist'))
)
