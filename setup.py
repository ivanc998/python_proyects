from setuptools import setup, find_packages

dist_name = 'Mathematics_functions'
description = 'Module with some mathematician fuctions'
manteiner = 'Ivan Gustavo Nieto'
url = 'https://github.com/ivanc998/python_proyects'

classifiers = ['Programming Language :: Python',
               'Programming Language :: Python :: 3.10.8']

if __name__ == "__main__":
    setup(name = dist_name,
          maintainer = manteiner, 
          description = description,
          packages = find_packages(),
          url = url,
          classifiers = classifiers,
          install_requires = ["numpy"])
