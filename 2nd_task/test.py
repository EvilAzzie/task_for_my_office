import pytest
from main_page import MainPage
from search_page import SearchPage
from my_office_page import MyOfficePage

class TestMyOffice():

    def test_can_find_my_office(self,browser):
        link = "https://spb.hh.ru/"
        self.page = MainPage(browser,link)
        self.page.open()
        self.page.should_be_search_field()
        self.page.make_search_request("мойофис")
        link = browser.current_url
        self.page = SearchPage(browser,link)
        self.page.should_be_search_page()
        self.page.is_my_office_present()
  
    def test_how_many_vacancies_in_current_region(self,browser):
        link = "https://spb.hh.ru/employer/213397"
        self.page = MyOfficePage(browser,link)
        self.page.open()
        self.page.is_current_region_vacancies_present()
        self.page.value_of_current_region_vacancies()
        self.page.report

    def test_can_find_qa_vacancy_in_current_region(self,browser):
        link = "https://spb.hh.ru/employer/213397"
        self.page = MyOfficePage(browser,link)
        self.page.open()
        self.page.open_information_technologies_vacancies()
        self.page.can_find_qa_vacancy()
