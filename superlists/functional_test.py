from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Ella goes to check out a cool new website
        #She goes to the home page
        self.browser.get('http://localhost:8000')

        #She notices the the page title and the header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #she is inivted to enter a to-do list item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #she types water the plants into a text box
        inputbox.send_keys('Water the plants')

        #when she hits enter the page refreashes and displays a list
        # "1 : Water the plants"
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Water the plants' for row in rows)
        )
        
        #There is still a text box prompting Ella to enter in another item
        #she enters "Run a mile" into the text box and presses enter

        #the homepage refreshed again and displays both items on her list

        #eidith realizes that there is a unique URL for her

        # she revisits this URL and her todo list is still there

        #happy, Ella goes back to watching protlandia
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
