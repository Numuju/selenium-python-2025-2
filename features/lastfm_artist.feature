Feature: Buscar un artista en last.fm y validar la fechar de su ultimo release
    Scenario: Validar la fecha del último release de Judeline
        Given el usuario esta en el home page de last.fm
        When el usuario busca al artista "Bruno Mars"
        And presiona el link del primer resultado
        Then la fecha del última release debe ser "3 October 2025"