from selenium import webdriver
import requests
from flask import Flask
# from app import create_app, db
from flask_testing import LiveServerTestCase
import os

class FunctionalTest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVE_URL'] =  "http://kuti.ml"
        app.config['KUTI_ADMIN_PASSWORD'] = os.environ.get("KUTI_ADMIN_PASSWORD")
        app.config['KUTI_ADMIN_USERNAME'] = os.environ.get("KUTI_ADMIN_USERNAME")
        return app

    def setUp(self):
        # self.app = create_app('testing')
        # self.app_context = self.app.app_context()
        # self.app_context.push()
        # db.create_all()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(40)

    def tearDown(self):
        # db.session.remove()
        # db.drop_all()
        # self.app_context.pop()
        self.driver.refresh()
        self.driver.quit()
