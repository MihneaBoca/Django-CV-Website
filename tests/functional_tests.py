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

        # He goes on the web page and clicks on CV Maker
        self.browser.get('http://localhost:8000')
        self.assertIn('Home', self.browser.title)
        time.sleep(5)
        self.browser.find_element_by_link_text('CV Maker').click()

        # He sees two buttons that say Create New CV or Edit CV and a form to enter his username
        # and since he doesn't have one he clicks on the first button
        self.browser.find_element_by_id('id_new_cv').click()

        self.assertIn('New CV', self.browser.title)

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
        # but he gets a prompt that says he hasn't entered his email and a username and
        # that he must enter them before submitting the CV
        self.browser.find_element_by_id('id_submit').click()
        time.sleep(2)

        # He enters them and is then able to submit his CV
        self.browser.find_element_by_id('id_username').send_keys('Adam01')
        self.browser.find_element_by_id('id_email').send_keys('adam_cart@gmail.com')
        self.browser.find_element_by_id('id_address').send_keys('18 Code Road, B21 2XS')
        self.browser.find_element_by_id('id_phone_number').send_keys('0734231234')
        self.browser.find_element_by_id('id_submit').click()
        time.sleep(5)

        # The website displays his brand new CV and after reading it he returns to the CV Maker menu
        self.browser.get('http://localhost:8000/new_cv/display')
        self.browser.find_element_by_id('id_menu_back').click()

        # He wants to edit his CV, but he accidentally clicks on New CV
        # And has to return to the selection page and click on Edit CV
        self.browser.find_element_by_id('id_new_cv').click()
        self.browser.find_element_by_id('id_new_back').click()
        self.browser.find_element_by_id('id_edit_cv').click()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
