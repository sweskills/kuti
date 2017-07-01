from base import FunctionalTest
import unittest


class RequirementsTest(FunctionalTest):

     def test_teacher_register(self):
         # Mr Adewale heard about a new teachers recruitment app,
         # He goes to open up it's home packages
         self.driver.get(self.app.config['LIVE_URL'])

         # He obseved that the site has content
         self.assertNotIn("The requested URL was not found on the server.", self.driver.find_element_by_tag_name("body").text)


if __name__=='__main__':
    unittest.main()
