
# coding: utf-8

# In[2]:


import nltk


# In[1]:


sentilex = open("C://Users//vitor//Downloads//SentiLex-PT01//SentiLex-lem-PT01.txt",'r')


# In[2]:


dic_palavra = {}
for i in sentilex.readlines():
    pos_ponto = i.find('.')
    palavra = (i[:pos_ponto])
    pol_pos = i.find('POL')
    polaridade = (i[pol_pos+4:pol_pos+6]).replace(';','')
    dic_palavra[palavra] = polaridade


# In[4]:


# print(dic_palavra)


# In[8]:


def Score_sentimento(frase):
    frase = frase.lower()
    l_sentimento = []
    for p in frase.split():
        l_sentimento.append(int(dic_palavra.get(p, 0)))
    score = sum(l_sentimento)
    if score > 0:
        return 'Positivo, Score:{}'.format(score)
    elif score == 0:
        return 'Neutro, Score:{}'.format(score)
    else:
        return 'Negativo, Score:{}'.format(score)


# In[9]:


Score_sentimento('Eu estou muito feliz hoje, porém, triste com a politica')


# In[10]:


Score_sentimento('Estou Muito Feliz hoje,super animado com o trabalho novo! :)')


# In[11]:


import csv


# In[67]:


with open('C:/Users/vitor/Documents/GetDataset/Infomoney/2018-10-02/dataset.csv', encoding="utf8") as csvfile:
    readCsv = csv.reader(csvfile, delimiter=",")
    for row in readCsv:
        print(row[2])
        Score_sentimento(row[2])

