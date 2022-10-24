
def busca(dados: list[int]) -> int:
    for i in range(0, len(dados), 2):
        if i == (len(dados) - 1):
            return dados[i]

        if dados[i] == dados[i + 1]:
            continue

        return dados[i]
    
    return -1


dados = [1, 1, 2, 2, 3, 3, 5, 7, 7, 8, 8, 10, 10]
print(busca(dados))
