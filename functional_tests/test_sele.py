from base import FunctionalTest
import unittest
from selenium.webdriver.common.keys import Keys


class RequirementsTest(FunctionalTest):

     def test_teacher_register(self):
         # Mr Adewale heard about a new teachers recruitment app,
         # He goes to open up it's home packages
         self.driver.get(self.app.config['LIVE_URL'])

         # He obseved that the site has content
         self.assertNotIn("The requested URL was not found on the server.", self.driver.find_element_by_tag_name("body").text)

    def test_admin_can_login(self):
        # an admin personnel wants to login and have access to the admin dasshboard
        self.driver.get(self.app.config['LIVE_URL'])
        sign_in_element = self.driver.find_element_by_id("sign_in")
        sign_in_element.click()
        password_box = self.driver.find_element_by_id("pass_box")
        name_box = self.driver.find_element_by_id("pass_box")
        submit_box = self.driver.find_element_by_id("login_submit")

        name_box.send_keys("")
        password_box.send_keys("")
        submit_box.click()

if __name__=='__main__':
    unittest.main()
