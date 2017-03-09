import os
import shutil
from unittest import TestCase

class IncipioTest(TestCase):

    def setUp(self):
        if not os.path.exists("container"): os.makedirs("container")


    def tearDown(self):
        shutil.rmtree("container")
