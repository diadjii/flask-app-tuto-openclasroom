import os

from flask_testing import LiveServerTestCase
from selenium import webdriver


class TestUserTakesTheTest(LiveServerTestCase):
    def create_app(self):
        # Fichier de config uniquement pour les tests.
        app.config.from_object('fbapp.tests.config')
        return app

    # Méthode exécutée avant chaque test
    def setUp(self):
        """Setup the test driver and create test users"""
        # Le navigateur est Firefox
        self.driver = webdriver.Firefox()
        # Ajout de données dans la base.
        models.init_db()

    # Méthode exécutée après chaque test
    def tearDown(self):
        self.driver.quit()
