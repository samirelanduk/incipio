import os
from unittest.mock import patch
from base import IncipioTest
from incipio.package import create_package, git_init, git_ignore

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


class PackageCreationParameterTests(IncipioTest):

    @patch("incipio.package.git_init")
    def test_git_init_called_by_default(self, mock_init):
        create_package("testpack", "container")
        mock_init.assert_called_with("container/testpack")


    @patch("incipio.package.git_init")
    def test_can_choose_not_to_git_init(self, mock_init):
        create_package("testpack", "container", git=False)
        self.assertFalse(mock_init.called)
