from base_page import BasePage
from locators import MyOfficePageLocators
import atexit

class MyOfficePage(BasePage):
            
    def is_current_region_vacancies_present(self):
        assert self.is_element_present(*MyOfficePageLocators.CURRENT_REGION_VACANCIES_LINK), "There's no current region vacancies."                       

    def value_of_current_region_vacancies(self):
        value_of_vacancies=self.browser.find_element(*MyOfficePageLocators.VALUE_OF_CURRENT_REGION_VACANCIES)        
        global message
        message=str(f"Value of vacancies in current region is {value_of_vacancies.text}")

    @atexit.register
    def report():
        print (message)

    def open_information_technologies_vacancies(self):      
        information_technologies_vacancies=self.browser.find_element(*MyOfficePageLocators.INFORMATION_TECHNOLOGIES_VACANCIES_LINK)
        information_technologies_vacancies.click()

    def can_find_qa_vacancy(self):      
        assert self.is_element_present(*MyOfficePageLocators.QA_VACANCY_LINK), "There's no vacancy 'Junior QA Automation Engineer'."
