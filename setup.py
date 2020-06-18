  
from distutils.core import setup
from setuptools import setup,setuptools
import os 
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme_file:
    readme = readme_file.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pyzohodocs',
    version='1.5',
    packages=setuptools.find_packages(),
    include_package_data=True,
    long_description_content_type= 'text/markdown',
    long_description=open('README.md').read(),
    description = "A Python Wrapper for the ZohoDocs API",
    author = "Vishnu Varthan Rao",
    author_email="vishnulatha006@gmail.com",
    url='https://github.com/VarthanV/pyzohodocs',
    install_requires=[
        "requests"
    ],
    license="MIT License",
    zip_safe=False,
    keywords='zohodocs,zoho,docs,zohocrm,docx,xlxs',
     classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],

)