# Nursery Application
#### Install dependencies
##### Compilers for Scipy

```
$ sudo apt-get install libblas3gf libc6 libgcc1 libgfortran3 liblapack3gf libstdc++6 build-essential gfortran python-all-dev libatlas-base-dev
```
#####Freetype and Libpng for Matplotlib
``` 
$ sudo apt-get install libfreetype6-dev
```

#### Work in a Virtualenv
Install pip
```
$ sudo apt-get install python-pip
```
Install virtualenv and virtualenvwrapper
```
$ sudo pip install virtualenv
$ sudo pip install virtualenvwrapper
```
Create a virtualenv
```
$ mkvirtualenv <env name>
```
*See virtualenvwrapper [docs](https://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html) to learn more about working in a virtualenv. Make sure you are always in the virtualenv during development*

####Clone the repository
Clone
```
$ git clone git@github.com:jayArnel/nursery-applicaiton.git
```
Go to the project's root directory and setup the project
```
$ pip install -r requirements.txt
$ python setup.py install
$ ./manage.py syncdb
```

# You're good to go!
