import os
from base import IncipioTest
from incipio.package import create_package

class BasicCreationTests(IncipioTest):

    def test_can_make_package_directory(self):
        create_package("testpack", "container")
        self.assertTrue(os.path.exists("container/testpack"))
