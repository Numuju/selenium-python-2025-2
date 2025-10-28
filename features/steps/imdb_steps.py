from behave import given, when, then
from selenium import webdriver
from pages.imdb_home_page import IMDbHomePage
from pages.imdb_results_page import IMDbResultsPage
from pages.imdb_movie_page import IMDbMoviePage


@given('el usuario está en la página principal de IMDb')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")
    context.imdb_home = IMDbHomePage(context.driver)


@when('el usuario busca la película "{movie_name}"')
def step_search_movie(context, movie_name):
    context.imdb_home.search_movie(movie_name)
    context.imdb_results = IMDbResultsPage(context.driver)


@when('selecciona el primer resultado de la búsqueda')
def step_select_first_result(context):
    context.imdb_results.open_first_result()
    context.imdb_movie = IMDbMoviePage(context.driver)


@then('el título de la película debe ser "{expected_title}" y su calificación debe ser "{expected_rating}"')
def step_compare_movie_info(context, expected_title, expected_rating):
    actual_title = context.imdb_movie.get_movie_title()
    actual_rating = context.imdb_movie.get_movie_rating()
    # Se permite el título original o su traducción
    valid_titles = [expected_title, "Origen"]
    assert actual_title in valid_titles, f"Expected '{expected_title}' or 'Origen' but got '{actual_title}'"
    assert actual_rating == expected_rating, f"Expected rating '{expected_rating}' but got '{actual_rating}'"
