"""
python-fleetio
--------------

Simple Python interface for FleetIO

"""
from setuptools import setup


setup(
    name='python-fleetio',
    version='0.0.1',
    url='https://github.com/Logic-gate/python-fleetio',
    license='MIT',
    author=['Amer Almadani'],
    author_email=['mad_dev@linuxmail.org'],
    description='Simple Python interface for FleetIO',
    long_description=file.read(open('README.md', 'r')),
    packages=['fleetio'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    tests_require=[
        'nose>=1.0',
    ],
    test_suite='nose.collector',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
