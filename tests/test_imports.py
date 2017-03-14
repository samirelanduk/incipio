from unittest import TestCase
import incipio

class PackageCreationImportTests(TestCase):

    def test_create_package_imported(self):
        from incipio.package import create_package
        self.assertIs(create_package, incipio.create_package)
