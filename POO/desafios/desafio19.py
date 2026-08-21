class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina = 1

        print(
            f"Você abriu o livro {self.titulo}, que possui "
            f"{self.paginas} páginas. Você está na página {self.pagina}."
        )

    def avancar_paginas(self, quantidade):
        if self.pagina == self.paginas:
            print("Você já está na última página.")
            return

        pagina_anterior = self.pagina
        self.pagina = min(self.pagina + quantidade, self.paginas)

        for numero in range(pagina_anterior + 1, self.pagina + 1):
            print(f"Página {numero} > ", end="")

        avancadas = self.pagina - pagina_anterior

        print(
            f"\nVocê avançou {avancadas} páginas "
            f"e agora está na página {self.pagina}."
        )

l1 = Livro('Kevin',20)
l1.avancar_paginas(6)