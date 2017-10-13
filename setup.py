try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = '''
An open source library for sending messages to Discord from Python 2.7 using Discords built in channel webhooks
'''

setup(name='discordhooks',
      description='Python library for using Discord Webhooks',
      long_description=long_description,
      license='BSD 3-clause "New" or "Revised"',
      version='1.0.0',
      author='Jordan Maxwell',
      maintainer='Jordan Maxwell',
      url='https://github.com/NxtStudios/DiscordHooks',
      packages=['discordhooks'],
      classifiers=[
          'Programming Language :: Python :: 2',
      ])