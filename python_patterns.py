# Solução p/ calculo de impostos 'procedural'
class Imposto():
  def __init__(self, tipo, valor_base):
    self.tipo = tipo
    self.valor_base = valor_base
    self.aliquota_iss = 5
    self.aliquota_ipi = 10

  def valor_retencao(self):
    if self.tipo == 'iss':
      return self.valor_base * (self.aliquota_iss/100)
    elif self.tipo == 'ipi':
      return self.valor_base * (self.aliquota_ipi/100)

valor_venda = 100
print(f'valor iss: {Imposto("iss", valor_venda).valor_retencao()}')
print(f'valor ipi: {Imposto("ipi", valor_venda).valor_retencao()}')

# Solução p/ calculo de impostos : OO com Strategy!
class NovoImposto(object):
  def __init__(self, valor_base):
    self.valor_base = valor_base

class ImpostoIss(NovoImposto):
  def __init__(self, valor_base):
    self.valor_base = valor_base
    self.aliquota = 5

  def valor_retencao(self):
    return self.valor_base * (self.aliquota/100)

class ImpostoIpi(NovoImposto):
  def __init__(self, valor_base):
    self.valor_base = valor_base
    self.aliquota = 10

  def valor_retencao(self):
    return self.valor_base * (self.aliquota/100)

valor_venda = 100
print(f'valor iss: {ImpostoIss(valor_venda).valor_retencao()}')
print(f'valor ipi: {ImpostoIpi(valor_venda).valor_retencao()}')



# Solução p/ calculo de impostos 'procedural'
class Venda():
  def __init__(self, valor, tipo):
    self.valor = valor
    self.tipo = tipo

vendaServico = Venda(100, 'servico')
vendaIndustria = Venda(100, 'industria')

imposto = None
if vendaServico.tipo == 'servico':
  imposto = ImpostoIss(vendaServico.valor)
elif vendaServico.tipo == 'industria':
  imposto = ImpostoIpi(vendaServico.valor)
print(f'sua retencao p/ vendaServico sera: {imposto.valor_retencao()}')

if vendaIndustria.tipo == 'servico':
  imposto = ImpostoIss(vendaIndustria.valor)
elif vendaIndustria.tipo == 'industria':
  imposto = ImpostoIpi(vendaIndustria.valor)
print(f'sua retencao p/ vendaIndustria sera: {imposto.valor_retencao()}')

# Solução p/ calculo de impostos : OO com Factory!
class ImpostoFactory():
  @staticmethod
  def create(tipo, valor):
    if vendaServico.tipo == 'servico':
      return ImpostoIss(valor)
    elif vendaServico.tipo == 'industria':
      return ImpostoIpi(valor)

vendaServico = Venda(100, 'servico')
vendaIndustria = Venda(100, 'industria')
print(f'sua retencao p/ vendaServico sera: {ImpostoFactory.create(vendaServico.tipo, vendaServico.valor).valor_retencao()}')
print(f'sua retencao p/ vendaIndustria sera: {ImpostoFactory.create(vendaIndustria.tipo, vendaIndustria.valor).valor_retencao()}')