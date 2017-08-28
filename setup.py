# setup.py for the PyHyphen hyphenation package
# (c) Dr. Leo (fhaxbox66 <at> gmail >dot< com)

from setuptools import setup, Extension


arg_dict = dict(
    name="PyHyphen",
    version="3.0.0",
    author="Dr. Leo",
    author_email="fhaxbox66@googlemail.com",
    url="https://bitbucket.org/fhaxbox66/pyhyphen",
    description="The hyphenation library of LibreOffice and FireFox wrapped for Python",
    long_description=open('README.rst', 'r').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: C',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic'
    ],
    packages=['hyphen', 'textwrap2'],
    ext_modules=[
        Extension('hyphen.hnj', ['src/hnjmodule.c',
                                 'src/hyphen.c',
                                 'src/hnjalloc.c'],
                  include_dirs=['include'])],
    install_requires=['appdirs', 'six'],
)


setup(**arg_dict)
