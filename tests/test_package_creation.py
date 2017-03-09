import os
from base import IncipioTest
from incipio.package import create_package

class BasicCreationTests(IncipioTest):

    def test_can_make_package_directory(self):
        create_package("testpack", "container")
        self.assertTrue(os.path.exists("container/testpack"))


    def test_package_must_be_str(self):
        with self.assertRaises(TypeError):
            create_package(100, "container")


    def test_location_must_be_str(self):
        with self.assertRaises(TypeError):
            create_package("testpack", 100)
