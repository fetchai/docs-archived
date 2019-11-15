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
    sass_manifests={
        'package': {
            'sass_path': '../../docs/sass',
            'css_path': '../../docs/css',
            'strip_extension': True,
        },
    },
    setup_requires=['libsass >= 0.6.0'],
    install_requires=['libsass >= 0.6.0'],
    entry_points={
        'mkdocs.themes': [
            'gitbook = mkdocs_gitbook',
        ]
    },
    zip_safe=False
)
