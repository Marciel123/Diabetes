

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

#Copiar o endereço do seu google drive onde esta rodando o projeto e o arquivo 'diabetes.csv' esta dentro.
dados = pd.read_csv("diabetes.csv")vírgula

#planilha.info()
nomesColunas = planilha.columns.to_list() #Nomes recebem todas as colunas e são colocadas numa lista
print("\n NOME DAS COLUNAS: \n",nomesColunas[:8])


###################importando os dados do csv ########################


'''#coleta os nomes das colunas
nomes_colunas = dados.columns.to_list()
tamanho = len(nomes_colunas)
nomes_colunas = nomes_colunas[:tamanho-1]
features = dados[nomes_colunas]
classes = dados['Outcome']
features.shape,classes.shape
st.write(nomes_colunas)
#dividir entre treino e teste

from sklearn.model_selection import train_test_split
features_treino,features_teste,classes_treino,classes_teste = train_test_split(features,classes,test_size=0.3,random_state=2)
from sklearn.tree import DecisionTreeClassifier
arvore = DecisionTreeClassifier()
