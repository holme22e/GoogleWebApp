from .base import ToDoFunctionalTest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class ToggleDoneTest(ToDoFunctionalTest):
    def toggle_todo_done(self, todo_text_list):
        for todo_text in todo_text_list:
            row = self.find_table_row(todo_text)
            row.find_element_by_tag_name('input').click()
        self.browser.find_element_by_id('toggle_done').click()

    def check_marked_off(self, todo_text):
        row = self.find_table_row(todo_text)
        try:
            row.find_elements_by_css_selector('.todo-done')
        except NoSuchElementException:
            self.fail("%s not marked done!" % (todo_text))

    def test_can_toggle_finished_items(self):
        #Edith makes a quick shoping list,
        #noticing a checkbox to toggle done ItemValidationTest
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('Buy peacock feathers')
        self.enter_a_new_item('Buy fishing line')

        checkbox_selector = 'input[type = "checkbox"]'
        checkboxes = self.browser.find_elements_by_css_selector(checkbox_selector)
        self.assertEqual( len(checkboxes), 2)

        #at the store Edits buys her feathers and marks them done on her List
        self.toggle_todo_done(['Buy peacock feathers', 'Buy fishing line'])


        #Edith returns home and opens her todo list and sees
        # that her list is still marked and crossed off
        current_list_url = self.browser.current_url
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(current_list_url)
        self.check_marked_off('Buy peacock feathers')
        self.check_marked_off('Buy fishing line')

        #she adds a todo item to tie her flys and marks them done on her list
        self.enter_a_new_item('Tie some flys')
        self.check_marked_off('Buy peacock feathers')
        self.check_marked_off('Buy fishing line')
        self.toggle_todo_done(['Tie some flys'])
        self.check_marked_off('Tie some flys')
