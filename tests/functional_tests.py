import os

from selenium import webdriver
import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager


class NewTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_access_website(self):
        # Adam is a student that wants to write a CV for future use,
        # he's heard there is a website where you can write your CV online

        # He goes to the homepage
        # browser = webdriver.Chrome(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cromedriver.exe'))
        # browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000')

        self.assertIn('Home', self.browser.title)

        # He sees the form he needs to complete in order to end up with a CV
        # He enters his name first
        input_fn = self.browser.find_element_by_id('id_first_name')
        input_ln = self.browser.find_element_by_id('id_last_name')
        self.assertEqual(
            input_fn.get_attribute('placeholder'),
            'Enter your First Name'
        )
        self.assertEqual(
            input_ln.get_attribute('placeholder'),
            'Enter your Last Name'
        )

        input_fn.send_keys('Adam')
        input_ln.send_keys('Cart')

        # He has no work experience yet so he decides to skip that part
        # Then he enters information about his education
        input_ed = self.browser.find_element_by_id('id_education')
        input_ed.send_keys('I studied at the University of Birmingham.')

        # After that he enters some of his skills
        input_sk = self.browser.find_element_by_id('id_skills')
        input_sk.send_keys('Java\nC++\nPython')
        time.sleep(2)

        # After he reads everything he has just written he decides to submit his CV,
        # but he gets a prompt that says he hasn't entered his email and address and
        # that he must enter them before submitting the CV
        self.browser.find_element_by_id('id_submit').click()
        time.sleep(2)
        self.assertIn('Home', self.browser.title)

        # He enters them and is then able to submit his CV
        self.browser.find_element_by_id('id_email').send_keys('adam_cart@gmail.com')
        self.browser.find_element_by_id('id_address').send_keys('18 Code Road, B21 2XS')
        self.browser.find_element_by_id('id_phone_number').send_keys('0734231234')
        self.browser.find_element_by_id('id_submit').click()
        time.sleep(20)

        # He decides to go an check if his CV was indeed saved on the website
        # He accesses the website again and sees that his CV was saved and can modify it again


if __name__ == '__main__':
    unittest.main(warnings='ignore')
