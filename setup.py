from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='kobe',
      version='0.0.1',
      url='https://github.com/lllmanriquelll/kobe-endpoint',
      license='MIT License',
      author='Luis Manrique',
      long_description=readme,
      long_description_content_type="text/markdown",
      author_email='manrique.luis@gmail.com',
      keywords='endpoint',
      description=u'Endpoint FastAPI',
      packages=['kobe'],
      install_requires=['fastapi==0.79.0', 'uvicorn==0.18.2',
                        'pytest==7.1.2', 'requests==2.28.1'], )
