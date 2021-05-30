from setuptools import setup

# ref: https://www.youtube.com/watch?v=RiWqigGW9cA

setup(name='spoken_to_written_english',
      version='0.2',
      description='Package to convert spoken english to writen english',
      author='Arun Sagar',
      author_email='asagar60@gmail.com',
      url='https://github.com/asagar60/spoken_to_written_english',
      packages=['spoken_to_written_english'],
      install_requires=[],
      license=open('LICENSE.txt').read(),
      long_description=open('README.md').read(),
      classifiers=[
            'License :: Free For Educational Use',
            'Programming Language :: Python :: 3.8',
            'Topic :: Text Processing :: General']
      )
