from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='python-file-datastore',
      version='1.0',
      description='File based datastore',
      url='https://github.com/njaveed/Datastore.git',
      author='Javeed',
      author_email='meetjaveed11@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
      packages=['python-file-datastore'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
		],
		python_requires='>=3.6',
      zip_safe=False)
