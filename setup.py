from setuptools import setup, find_packages

setup(
    name='nursery-application,
    version='1.0',
    packages=find_packages(),
    license='BSD License',
    author='Jay Arnel Bilocura',
    author_email='jdbilocura@up.edu.ph',
    install_requires=['django==1.8.1',
                      'coverage==3.7.1',
                      'scikit-learn==0.16.1',
                      'scipy==0.15.1',
                      'numpy==1.9.2',
                      'matplotlib==1.4.3',
                      ]
)
