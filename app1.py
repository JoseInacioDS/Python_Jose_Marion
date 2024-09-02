#Ordenação natural e ordenação customizada
import re

# Função para ordenação natural
def natural_key(s):
    return [int(texto) if texto.isdigit() else texto.lower() for texto in re.split('([0-9]+)', s)]

# Dados para ordenação
data = ['arquivo1', 'arquivo2', 'arquivo4', 'arquivo5', 'arquivo6', 'arquivo3']
data2 = ["Josias Nascimento", "Alberto Torres", "Gerivaldo Batista", "Anderson Moreira", "Jhon Wick"]

# Ordenação natural
ordenacao_natural = sorted(data, key=natural_key)

# Ordenação customizada
ordenacao_customizada = sorted(data2, key=len)

print("Ordenação natural:", ordenacao_natural)
print("Ordenação customizada:", ordenacao_customizada)
