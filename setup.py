from setuptools import setup, find_packages

import os
import sys


PYTHON3 = sys.version_info > (3, )
HERE = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open(os.path.join(HERE, 'README.md')) as f:
        return f.read()


def get_version():
    with open(os.path.join(HERE, 'git_cloner/__init__.py'), 'r') as f:
        content = ''.join(f.readlines())
    env = {}
    if PYTHON3:
        exec(content, env, env)
    else:
        compiled = compile(content, 'get_version', 'single')
        eval(compiled, env, env)
    return env['__version__']


setup(
  name='git-cloner',
  version=get_version(),
  description='Batch clone projects from GitLab server',
  long_description=readme(),
  long_description_content_type='text/markdown',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: System :: Distributed Computing',
    'Topic :: System :: Networking',
  ],
  keywords='git clone',
  url='https://github.com/gebing/git-clone',
  license='Apache License 2.0',
  author='gebing',
  author_email='gebing@foxmail.com',
  packages=find_packages(),
  scripts=['git-clone'],
  include_package_data=True,
  platforms = "any",
  install_requires=[
  ],
)
