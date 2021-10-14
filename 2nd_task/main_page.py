from base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):
    
    def should_be_search_field(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_FIELD), "Missing search field."
    
    def make_search_request(self,request):
        search_field=self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        search_field.send_keys(str(request))
        search_button=self.browser.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()
