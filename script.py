import pandas as pd
import matplotlib.pyplot a plt
#==============================
#Leitura dos dados
#==============================
dados+ pd.read_csv('dados/dados.csv')

#==============================
#VIsualização incial
#==============================

print(dados.head(10)

#==============================
#Histograma
#==============================
dados['nota'].hist(bins=5)
      plt.xlabel('notas')
      plt.ylabel('quantidade')
      plt.savefix('histo.png')
      olt.clf() #limpa o gráfico antes do proximo
#==============================
#Boxplot
#==============================

      dados.boxplot.(column=['nota'])
      plt.title('Boxplot das notas')
      plt.savefig('boxplot.png')
      plt.clf()
#==============================
#Estatisticas
#==============================
print("média idade:", dados['idade'].mean())
      print("mediana:".dados['nota'].median())
      print("desvio padrão:", dados{'nota].std())'
