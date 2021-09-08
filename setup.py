import setuptools

with open('README.md', 'r') as fh:
    long_descrption = fh.read()

setuptools.setup(
    name='pds'
    version_config=True,
    setup_requires=['setuptools-git-versioning'],
    author='Lukas Halbritter',
    author_email='halbi93@gmx.de',
    description='Datastructures implemented in Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
    )
