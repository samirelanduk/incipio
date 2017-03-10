import os
import subprocess

def create_package(package, location, git=True):
    if not isinstance(package, str):
        raise TypeError("package name must be str, not '%s'" % str(package))
    if not isinstance(location, str):
        raise TypeError("location must be str, not '%s'" % str(location))
    os.makedirs("%s%s%s" % (location, os.path.sep, package))
    if git:
        git_init(os.path.sep.join([location, package]))
        git_ignore(os.path.sep.join([location, package]))


def git_init(location):
    if not isinstance(location, str):
        raise TypeError("location must be str, not '%s'" % str(location))
    with open(os.devnull, 'w') as FNULL:
        subprocess.call("git init %s" % location, shell=True, stdout=FNULL)


def git_ignore(location, ignore=None):
    ignore = ignore if ignore else []
    with open(os.path.sep.join([location, ".gitignore"]), "w") as f:
        f.write("\n".join([
         "*.pyc",
         "__pycache__",
         ".DS_Store",
         "*env",
         "build",
         "_static",
         "_templates",
         "dist",
         "*.egg-info",
        ] + ignore))
