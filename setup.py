from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    packages=find_packages(),
    include_package_data=True,
    sass_manifests={
        '': {
            'sass_path': './docs/sass',
            'css_path': './docs/css',
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
