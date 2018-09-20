from setuptools import setup, find_packages

setup(name='tst',
      version='0.9a14',
      description='TST Student Testing',
      url='http://github.com/daltonserey/tst',
      author='Dalton Serey',
      author_email='daltonserey@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      scripts=[
        'bin/gen2.py',
        'bin/runjava',
        'bin/tst',
        'etc/tst.completion.sh',
        'commands/tst-test',
        'commands/tst-check',
        'commands/tst-completion',
        'commands/tst-config',
        'commands/tst-gentests',
        'commands/tst-status',
        'commands/tst-update',
        'commands/tst-checkout',
        'commands/tst-commit',
        'commands/tst-delete',
        'commands/tst-download',
        'commands/tst-list',
        'commands/tst-login',
        'commands/tst-new',
        'commands/tst-release',
      ],
      install_requires=[
        'pyyaml',
        'requests'
      ],
      zip_safe=False)
