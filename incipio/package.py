import os

def create_package(package, location):
    os.makedirs("%s%s%s" % (location, os.path.sep, package))
