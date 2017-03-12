import os
from datetime import datetime
import shutil
from unittest import TestCase

class IncipioTest(TestCase):

    def setUp(self):
        if not os.path.exists("container"): os.makedirs("container")
        self.current_year = datetime.now().year


    def tearDown(self):
        shutil.rmtree("container")
