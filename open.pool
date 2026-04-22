class using:
    def __init__(self, resource):
         """
        Recebe o objeto de recurso (ex: open()).
        Suporta qualquer modo: 'r', 'w', 'a', 'rb', 'wb', etc.
        """
        self.resource = resource

    def __enter__(self):
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Garante o fechamento independente de erro
        if hasattr(self.resource, 'close'):
            self.resource.close()

# 1. Modo 'a' (Append) - Adiciona sem deletar o anterior
using open('log.txt', 'a', encoding='utf-8') as file:
    file.write("Nova linha adicionada sem apagar o resto!\n")

# 2. Modo 'w' (Write) - Sobrescreve tudo
using open('config.txt', 'w', encoding='utf-8') as file:
    file.write("Resetando o arquivo.\n")

# 3. Modo 'r' (Read) - Apenas leitura
using open('log.txt', 'r', encoding='utf-8') as file:
    dados = file.read()
