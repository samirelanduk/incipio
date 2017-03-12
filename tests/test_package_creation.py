import os
from unittest.mock import patch
from base import IncipioTest
from incipio.package import create_package, git_init, git_ignore, create_env
from incipio.package import create_python_package, create_test_directory
from incipio.package import create_license

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



class GitInitTests(IncipioTest):

    def test_can_initialise_git_repository(self):
        git_init("container")
        self.assertIn(".git", os.listdir("container"))


    def test_git_init_needs_str_location(self):
        with self.assertRaises(TypeError):
            git_init(100)



class GitIgnoreTests(IncipioTest):

    def test_can_create_gitignore(self):
        git_ignore("container")
        self.assertIn(".gitignore", os.listdir("container"))


    def test_gitignore_has_basic_stuff(self):
        git_ignore("container")
        with open("container/.gitignore") as f:
            contents = f.read()
        self.assertIn("__pycache__", contents)
        self.assertIn("*.pyc", contents)


    def test_can_add_own_lines_to_gitignore(self):
        git_ignore("container", ignore=["noA", "noB"])
        with open("container/.gitignore") as f:
            lines = f.readlines()
        self.assertEqual(lines[-2], "noA\n")
        self.assertEqual(lines[-1], "noB")


    def test_custom_ignore_must_be_list(self):
        with self.assertRaises(TypeError):
            git_ignore("container", ignore=("noA", "noB"))



class VenvTests(IncipioTest):

    @patch("subprocess.call")
    def test_can_create_virtual_env(self, mock_call):
        create_env("container")
        self.assertEqual(
         mock_call.call_args[0][0],
         "virtualenv -p python3 container/env"
        )


    @patch("subprocess.call")
    def test_can_create_virtual_env_with_custom_name(self, mock_call):
        create_env("container", name="speshenv")
        self.assertEqual(
         mock_call.call_args[0][0],
         "virtualenv -p python3 container/speshenv"
        )



class PythonPackageCreationTests(IncipioTest):

    def test_can_make_python_package(self):
        create_python_package("container", "packagename")
        self.assertIn("packagename", os.listdir("container"))
        self.assertIn("__init__.py", os.listdir("container/packagename"))


    def test_init_has_version(self):
        create_python_package("container", "packagename")
        with open("container/packagename/__init__.py") as f:
            self.assertIn('version = "0.1.0"', f.read())


    def test_init_can_have_name(self):
        create_python_package("container", "packagename", author="Sam")
        with open("container/packagename/__init__.py") as f:
            data = f.read()
            self.assertIn('version = "0.1.0"', data)
            self.assertIn('author = "Sam"', data)



class TestDirectoryCreationTests(IncipioTest):

    def test_can_make_test_directory(self):
        create_test_directory("container")
        self.assertIn("tests", os.listdir("container"))
        self.assertIn("__init__.py", os.listdir("container/tests"))



class LicenseCreationTests(IncipioTest):

    def test_can_make_mit_license(self):
        create_license("container", "mit", "Sam")
        self.assertIn("LICENSE", os.listdir("container"))
        with open("container/LICENSE") as f:
            data = f.read()
            self.assertIn("MIT", data)
            self.assertIn("Sam", data)
            self.assertIn(str(self.current_year), data)


    def test_can_make_apache_license(self):
        create_license("container", "apache", "Sam")
        self.assertIn("LICENSE", os.listdir("container"))
        with open("container/LICENSE") as f:
            data = f.read()
            self.assertIn("apache", data)
            self.assertIn("Sam", data)
            self.assertIn(str(self.current_year), data)


    def test_can_make_gnu_license(self):
        create_license("container", "gnu", "Sam")
        self.assertIn("LICENSE", os.listdir("container"))
        with open("container/LICENSE") as f:
            data = f.read()
            self.assertIn("GNU", data)
            self.assertIn("Sam", data)
            self.assertIn(str(self.current_year), data)


    def test_disallowed_licenses(self):
        with self.assertRaises(ValueError):
            create_license("container", "wrong", "Sam")



class PackageCreationParameterTests(IncipioTest):

    @patch("incipio.package.git_init")
    def test_git_init_called_by_default(self, mock_init):
        create_package("testpack", "container")
        mock_init.assert_called_with("container/testpack")


    @patch("incipio.package.git_init")
    def test_can_choose_not_to_git_init(self, mock_init):
        create_package("testpack", "container", git=False)
        self.assertFalse(mock_init.called)


    @patch("incipio.package.git_ignore")
    def test_git_ignore_called_by_default(self, mock_ignore):
        create_package("testpack", "container")
        mock_ignore.assert_called_with("container/testpack")


    @patch("incipio.package.git_ignore")
    def test_can_choose_not_to_git_init(self, mock_ignore):
        create_package("testpack", "container", git=False)
        self.assertFalse(mock_ignore.called)


    @patch("incipio.package.create_env")
    def test_create_env_not_called_by_default(self, mock_env):
        create_package("testpack", "container")
        self.assertFalse(mock_env.called)


    @patch("incipio.package.create_env")
    def test_can_choose_to_create_env(self, mock_env):
        create_package("testpack", "container", env=True)
        mock_env.assert_called_with("container/testpack")


    @patch("incipio.package.create_env")
    def test_can_provide_env_name(self, mock_env):
        create_package("testpack", "container", env="macenv")
        mock_env.assert_called_with("container/testpack", name="macenv")


    @patch("incipio.package.create_python_package")
    def test_py_package_creator_called(self, mock_creator):
        create_package("testpack", "container")
        mock_creator.assert_called_with(
         "container/testpack", "testpack", author=None
        )


    @patch("incipio.package.create_python_package")
    def test_py_package_creator_given_name(self, mock_creator):
        create_package("testpack", "container", author="Sam")
        mock_creator.assert_called_with(
         "container/testpack", "testpack", author="Sam"
        )


    @patch("incipio.package.create_test_directory")
    def test_test_creator_called_by_default(self, mock_creator):
        create_package("testpack", "container")
        mock_creator.assert_called_with("container/testpack")


    @patch("incipio.package.create_test_directory")
    def test_can_choose_not_to_create_tests(self, mock_creator):
        create_package("testpack", "container", test=False)
        self.assertFalse(mock_creator.called)


    @patch("incipio.package.create_license")
    def test_license_creator_called_by_default(self, mock_creator):
        create_package("testpack", "container")
        mock_creator.assert_called_with("container/testpack", "mit", "")


    @patch("incipio.package.create_license")
    def test_can_choose_not_to_create_license(self, mock_creator):
        create_package("testpack", "container", license=False)
        self.assertFalse(mock_creator.called)


    @patch("incipio.package.create_license")
    def test_license_creator_can_vary_license(self, mock_creator):
        create_package("testpack", "container", license="gnu")
        mock_creator.assert_called_with("container/testpack", "gnu", "")


    @patch("incipio.package.create_license")
    def test_license_creator_can_be_given_author(self, mock_creator):
        create_package("testpack", "container", author="Sam")
        mock_creator.assert_called_with("container/testpack", "mit", "Sam")
