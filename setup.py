import os
from setuptools import setup
 
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
 
# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name = 'django-rest-framework-proxy-gateway',
    version = '1.0.0',
    packages = ['rest_framework_proxy_gateway', 'tests'],
    include_package_data = True,
    license = 'BSD License',
    description = 'Extends django-rest-framework-proxy to limit the http verbs.',
    long_description = README,
    install_requires=[
          'django-rest-framework-proxy>=1.6.0,<1.7.0',
      ],
    test_suite='tests',
    url = 'http://www.example.com/',
    author = 'Gordon Collins',
    author_email = 'gordon.collins@excella.com',
    classifiers =[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)