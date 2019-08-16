from setuptools import setup

setup(
    name='tm-py',
    description='Task Manager',
    version='0.0',
    url='https://github.com/mobileAppSoft/tm.py',
    author='Dzmitry Shulhin (https://github.com/dz-s)',
    author_email='shulhindvst@gmail.com',
    packages=['tm-py'],
    install_requires=[
        'click',
        'GitPython'
    ],
    zip_safe=False,
    license='MIT',
    long_description=open('README.md').read(),
)
