Install pyqt on mac
```bash
  $ brew install pyqt --with-python3
  
```

sip will be automatically installed as dependency

Python modules have been installed and Homebrew's site-packages is not
in your Python sys.path, so you will not be able to import the modules 
this formula installed. If you plan to develop with these modules,
please run:

# For python 2.7

```
  $ mkdir -p /Users/boyuan/Library/Python/2.7/lib/python/site-packages
  $ echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> 
    /Users/boyuan/Library/Python/2.7/lib/python/site-packages/homebrew.pth
```    
    
# For Python 3.5
  $ mkdir -p /Users/boyuan/Library/Python/2.7/lib/python/site-packages
  $ echo 'import site; site.addsitedir("/usr/local/lib/python3.5/site-packages")' >> 
    /Users/boyuan/Library/Python/3.5/lib/python/site-packages/homebrew.pth

# To install PyQt4 on Linux
  $ sudo apt-get install python-qt4

# or
  $ sudo pip install python-qt4
  
# You can also get a wheel file for pip installation at: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4
