Feature: Buscar una película en IMDb y validar su calificación
    Scenario: Validar el título y la calificación de la película Inception
        Given el usuario está en la página principal de IMDb
        When el usuario busca la película "Inception"
        And selecciona el primer resultado de la búsqueda
        Then el título de la película debe ser "Inception" y su calificación debe ser "8,8"
