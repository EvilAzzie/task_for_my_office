from base_page import BasePage
from locators import SearchPageLocators

class SearchPage(BasePage):
    
    def should_be_search_page(self):        
        assert "search" in self.browser.current_url, "This URL not for search page"
    
    def switch_to_companies_search(self):
        companies_button=self.browser.find_element(*SearchPageLocators.SELECT_COMPANIES_BUTTON)
        companies_button.click()
                         
    def is_my_office_present(self):
        assert self.is_element_present(*SearchPageLocators.MY_OFFICE_LINK), "Missing 'Мой ОФис' link in companies list."
