```bash
# make sure twine is installed
$ pip install twine

# can install on your own system
$ python setup.py install

# Alternatively, can create distribution directory without local install
$ python setup.py sdist
i

# Register on TestPyPi: https://test.pypi.org/account/register/ 
# Will need to do email verification before next step will work 

# Now use twine to upload
# You will be prompted for username and password
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Now install from pip (uninstall first if you installed locally)
# This is more complicated because we are using testpypi =)
$ pip install --extra-index-url https://testpypi.python.org/simple roman
```
