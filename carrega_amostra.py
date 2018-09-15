import pandas as pd

def carregar():

  df = pd.read_csv('amostra-ml.csv')
  x_df = df[['carne', 'vegetais', 'genero']]
  y_df = df[['gosta_cerveja']]

  return x_df.values, y_df.values