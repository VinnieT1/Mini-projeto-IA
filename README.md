# Mini-projeto-IA
Mini projetos para a matéria de Inteligência Artificial
## Questão 3
Na terceira pergunta, empregamos o algoritmo ID3 e armazenamos a árvore de decisão em um formato JSON 
com a seguinte estrutura:  
![alt text](https://github.com/VinnieT1/Mini-projeto-IA/blob/main/jsoncrack.com.png)  
Em essência, o `JSON` descreve um vértice, identificando se ele é uma folha ou um ponto de decisão. 
Se for uma folha, ele possui a chave "Risco" com seu valor correspondente representando o resultado. 
Caso seja um ponto de decisão, o objeto contém a chave "pergunta" com o valor correspondente ao critério 
de decisão daquele vértice, e depois segue uma matriz de várias subárvores, cada uma delas representando 
as opções de decisão disponíveis nas arestas.  
Veja o JSON:  
```
{
  "pergunta": "Renda",
  "respostas": [
    {
      "0a15": {
        "Risco": "Alto"
      }
    },
    {
      "15a35": {
        "pergunta": "Historia de Credito",
        "respostas": [
          {
            "Desconhecida": {
              "pergunta": "Divida",
              "respostas": [
                {
                  "Alta": {
                    "Risco": "Alto"
                  }
                },
                {
                  "Baixa": {
                    "Risco": "Moderado"
                  }
                }
              ]
            }
          },
          {
            "Boa": {
              "Risco": "Moderado"
            }
          },
          {
            "Ruim": {
              "Risco": "Alto"
            }
          }
        ]
      }
    },
    {
      "Acima35": {
        "pergunta": "Historia de Credito",
        "respostas": [
          {
            "Desconhecida": {
              "Risco": "Baixo"
            }
          },
          {
            "Ruim": {
              "Risco": "Moderado"
            }
          },
          {
            "Boa": {
              "Risco": "Baixo"
            }
          }
        ]
      }
    }
  ]
}
```
### Execução
Para executá-lo, é suficiente executar o script em Python, desde que o banco de dados esteja armazenado no mesmo diretório com o nome `dados.csv`.  
No diretório `terceiro`, realize a execução do seguinte comando:  
* `python3 main.py`
