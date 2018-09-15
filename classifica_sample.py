# pip install scipy
# pip install numpy
# pip install sklearn
from sklearn.naive_bayes import MultinomialNB

# [come carne? come vegetais? é homem?]
dados = []
dados.append([1, 0, 1])
dados.append([1, 0, 1])
dados.append([1, 0, 0])
dados.append([1, 1, 0])
dados.append([1, 0, 1])
dados.append([1, 0, 1])
dados.append([1, 0, 0])
dados.append([1, 1, 0])
dados.append([1, 1, 1])
dados.append([1, 1, 0])
dados.append([0, 1, 0])
dados.append([0, 1, 1])
dados.append([1, 1, 1])
dados.append([1, 1, 0])
dados.append([0, 1, 0])
dados.append([0, 1, 1])

marcacoes = ([1]*10) + ([0]*6)

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

_1cervejeiro  = [1, 1, 1]
_2cervejeiro  = [1, 0, 0]
_1leiteiro    = [0, 1, 1]
_2leiteiro    = [0, 1, 0]

dados_teste = [_1cervejeiro, _2cervejeiro, _1leiteiro, _2leiteiro]
marcacoes_teste = [1, 1, 0, 0]

resultado = modelo.predict(dados_teste)
diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(dados_teste)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(resultado)
print(taxa_de_acerto)
