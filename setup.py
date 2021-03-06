from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(name="python-messaging",
      version='0.5.9',
      description='SMS/MMS encoder/decoder',
      license=open('COPYING').read(),
      packages=find_packages(),
      install_requires=['nose'],
      zip_safe=True,
      test_suite='nose.collector',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Topic :: Communications :: Telephony',
        ],
      **extra
)
