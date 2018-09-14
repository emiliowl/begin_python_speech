'''
'' Um pouco de O.O. (básica)
'''
class Pessoa():
  pass

p = Pessoa()
print(p)

# construtor!
class PessoaConstrutor():
  def __init__(self, nome):
    self.nome = nome

p2 = PessoaConstrutor('Maria')
print(p2)
print(p2.nome)

# object at <<0x04D70F10>> ????
class PessoaStr():
  def __init__(self, nome):
    self.nome = nome

  def __str__(self):
    return f'eu sou o {self.nome}'

pstr = PessoaStr('Joao')
print(pstr)
print(pstr.nome)

# atributos privados!
class PessoaPvt():
  def __init__(self, nome):
    self.__nome = nome

  def __str__(self):
    return f'eu sou o {self.__nome}'

ppvt = PessoaPvt('Pedro')
print(ppvt)
# print(p4.nome) Ouch!
# print(p4.__nome) Ouch(2)!

# Getter e Setter
class PessoaGet():
  def __init__(self, nome):
    self.__nome = nome

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, val):
    self.__nome = val

  def __str__(self):
    return f'eu sou o {self.__nome}'

pget = PessoaGet('Andre')
print(pget)
print(pget.nome)
pget.nome = 'André Dois'
print(pget)
print(pget.nome)

# Herança
class PessoaH(object):
  def __init__(self, nome):
    self._nome = nome

  def __str__(self):
    return f'eu sou o {self._nome}'

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, val):
    self._nome = val

class Homem(PessoaH):
  def __init__(self, nome, cpf):
    self._nome = nome
    self.cpf = cpf
  
  def __str__(self):
    return f'eu sou a pf: {self.nome}, cpf: {self.cpf}'

homem = Homem('Joao da Silva', 373)
print(homem)
print(homem.nome)
print(homem.cpf)
homem.nome = 'Joao da Silva ...'
print(homem)


# Herança múltipla!
class PessoaMulher(object):
  def __init__(self, inteligencia):
    self._inteligencia = inteligencia

  @property
  def inteligencia(self):
    return self._inteligencia

  @inteligencia.setter
  def inteligencia(self, val):
    self._inteligencia = val

class Mulher(PessoaH, PessoaMulher):
  def __init__(self, nome, cpf, inteligencia):
    self._nome = nome
    self._inteligencia = inteligencia
    self.cpf = cpf
  
  def __str__(self):
    return f'eu sou a pf: {self.nome}, cpf: {self.cpf}, com inteligencia {self.inteligencia}'

mulher = Mulher('Maria da Silva', 373, True)
print(mulher)
print(mulher.nome)
print(mulher.cpf)
mulher.nome = 'Maria da Silva ...'
mulher.inteligencia = False
print(mulher)

# Objetos python podem aprender coisas novas!
# print(homem.inteligencia) Ai !!
homem.inteligencia = True
print(f'{homem.nome} agora com inteligencia {homem.inteligencia}') # aprendeu bem :)