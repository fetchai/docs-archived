from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name="mkdocs-gitbook",
    version=VERSION,
    url='https://gitlab.com/lramage/mkdocs-gitbook-theme',
    license='Apache License, Version 2.0',
    description='Default theme for GitBook for Mkdocs',
    author='Lucas Ramage',
    author_email='ramage.lucas@protonmail.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'gitbook = mkdocs_gitbook',
        ]
    },
    zip_safe=False
)
