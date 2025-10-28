from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IMDbMoviePage(BasePage):
    # 🏷️ Locators para título y calificación
    MOVIE_TITLE = (By.CSS_SELECTOR, "span.hero__primary-text")
    MOVIE_RATING = (By.CSS_SELECTOR, "span.sc-4dc495c1-1")

    def get_movie_title(self):
        return self.find_element(self.MOVIE_TITLE).text

    def get_movie_rating(self):
        return self.find_element(self.MOVIE_RATING).text
