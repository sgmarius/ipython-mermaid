import setuptools
from distutils.core import setup

setup(
  name = 'ipython-mermaid-magic',
  packages = ['MermaidMagic'],
  version = '0.3',
  license='MIT',
  description = 'Cell magic to allow for usage of mermaid notation inside Databricks',
  author = 'Marius Sandu',
  author_email = 'marius@ltng-bi.com',
  url = 'https://github.com/sgmarius/ipython-mermaid',
  download_url = 'https://github.com/sgmarius/ipython-mermaid/blob/main/dist/ipython-mermaid-magic-0.2.tar.gz',
  keywords = ['IPython', 'Mermaid'],
  install_requires=[
          'IPython',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ]
)