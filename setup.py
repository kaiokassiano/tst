from setuptools import setup, find_packages
import codecs

with codecs.open('VERSION', encoding='utf-8', mode='r') as fv:
    version = fv.read().strip()

setup(name='tst',
      version=version,
      description='TST Student Testing',
      url='http://github.com/daltonserey/tst',
      author='Dalton Serey',
      author_email='daltonserey@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      scripts=[
        'bin/runjava',
        'bin/tst',
        'commands/tst-test',
        'commands/tst-completion',
        'commands/tst-config',
        'commands/tst-status',
        'commands/tst-checkout',
        'commands/tst-checkout2',
        'commands/tst-delete',
        'commands/tst-new',
      ],
      install_requires=[
        'pyyaml>=5.1',
        'requests',
        'cachecontrol[filecache]'
      ],
      entry_points = {
        'console_scripts': [
            'tst=tst.commands:main',
        ]
      },
      zip_safe=False)
