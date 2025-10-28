from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IMDbResultsPage(BasePage):
    FIRST_RESULT = (By.CSS_SELECTOR, "ul>li a.ipc-metadata-list-summary-item__t")

    def open_first_result(self):
        self.click(self.FIRST_RESULT)
