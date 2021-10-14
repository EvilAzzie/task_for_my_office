from selenium.webdriver.common.by import By

class MainPageLocators ():
    SEARCH_FIELD=(By.CSS_SELECTOR, 'div.supernova-search-group input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'div.supernova-search-group button')
    PARAMETRIZE_SEARCH_BUTTON = (By.CSS_SELECTOR, 'div.supernova-search-group span')

class SearchPageLocators ():
    SELECT_COMPANIES_BUTTON = (By.CSS_SELECTOR, 'div.supernova-navi-search-tab:last-child')
    FOUND_COMPANIES_LINKS = (By.CSS_SELECTOR, 'table.l a')
    MY_OFFICE_LINK = (By.XPATH, "//a[contains(text(),'МойОфис')]")

class MyOfficePageLocators ():
    CURRENT_REGION_VACANCIES_LINK = (By.XPATH, "//span[contains(text(),'Вакансии в текущем регионе')]")
    VALUE_OF_CURRENT_REGION_VACANCIES = (By.CSS_SELECTOR, 'h4.bloko-header-section-3 span.company-vacancies-hint')
    INFORMATION_TECHNOLOGIES_VACANCIES_LINK = (By.XPATH, "//span[contains(text(),'Информационные технологии')]")
    QA_VACANCY_LINK = (By.XPATH, "//a[contains(text(),'Junior QA Automation Engineer')]")
