# pip install scipy
# pip install numpy
# pip install sklearn
from sklearn.naive_bayes import MultinomialNB
from carrega_amostra import carregar

dados = []
dados.append([1, 0, 1])
dados.append([1, 0, 1])
dados.append([1, 0, 1])
dados.append([1, 1, 1])
dados.append([1, 0, 1])
dados.append([1, 0, 1])
dados.append([1, 0, 1])
dados.append([1, 1, 0])
dados.append([1, 1, 1])
dados.append([1, 1, 0])
dados.append([0, 1, 0])
dados.append([0, 1, 1])
dados.append([1, 1, 1])
dados.append([1, 1, 0])
dados.append([0, 1, 0])
dados.append([0, 1, 0])
marcacoes = ([1]*10) + ([0]*6)

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

X, Y = carregar()

resultado = modelo.predict(X)
diferencas = resultado - Y.flatten()

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(X)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(resultado)
print(taxa_de_acerto)