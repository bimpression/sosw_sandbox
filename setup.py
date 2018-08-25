from setuptools import setup


setup(name='sosw',
      version='0.1',
      description='Serverless Orchestrator of Serverless Workers',
      url='http://github.com/bimpression/sosw',
      author='Nikolay Grishchenko',
      author_email='nikolay@bimpression.com',
      license='MIT',
      classifiers=[
          'Operating System :: Other OS',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development'
      ],
      packages=['sosw'],
      install_requires=[
          'boto3',
      ],
      zip_safe=False)
