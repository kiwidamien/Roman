import setuptools

setuptools.setup(
    name="roman",
    version="0.1.0",
    url="https://github.com/kiwidamien/roman",
    author="Damien Martin",
    author_email="damien.j.martin@gmail.com",
    description="Allows conversion of Roman numerals to ints (and vice versa)",
    long_description=open('DESCRIPTION.rst').read(),
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
    package_data={'': ['data/*.csv']},
)
