# Mini-projeto-IA
Mini projetos para a matéria de Inteligência Artificial

O Expert Sinta se destaca por fornecer uma interface gráfica intuitiva que permite aos usuários construir sua base de conhecimento de forma visual e interativa. Por outro lado, nossa solução adota uma abordagem diferente, utilizando um arquivo JSON como meio de armazenamento e representação da base de conhecimento.  
Uma característica distintiva do nosso programa é a capacidade de gerar explicações em linguagem natural para as conclusões que produz. Isso significa que não apenas apresenta os resultados, mas também fornece uma narrativa compreensível e descritiva sobre como chegou a essas conclusões, tornando a interpretação e a tomada de decisões mais acessíveis aos usuários.  
Portanto, enquanto o Expert Sinta enfoca a construção visual da base de conhecimento, nossa solução se concentra na representação por meio de JSON e na entrega de explicações detalhadas em linguagem natural para maior transparência e entendimento das conclusões.  

As bases de conhecimento do Expert Sinta estão localizadas em suas respectivas pastas de questões.

## Questão 1
Na primeira questão, utilizamos o script de engenho de inferência para transformar as variáveis em proposições booleanas, construindo condições para cada conclusão das regras SE/ENTÃO, as quais estão localizadas em um arquivo JSON. O algoritmo faz forwards inference a toda resposta de pergunta, as quais são respondidas via terminal. Ao chegar em uma conclusão de animal (as quais são classificadas como objetivo final no arquivo final.json), o algoritmo para e dá o resultado de sua inferência, dando o animal encontrado e as justificativas por trás dessa inferência.

### Execução
Para executá-lo, é suficiente executar o script em Python.
No diretório `primeiro`, realize a execução do seguinte comando:  
* `python3 engenho.py`

## Questão 2
Na segunda questão, as variáveis multivaloradas foram adaptadas para variáveis booleanas e funcionam da mesma maneira que a primeira questão: as respostas das perguntas levam a forwards inference que, ao chegar em uma conclusão final, dá o resultado do diagnóstico e justifica essa decisão. Além disso, receita-se analgésico caso haja dor de cabeça.

### Execução
Para executá-lo, é suficiente executar o script em Python.
No diretório `segundo`, realize a execução do seguinte comando:  
* `python3 engenho.py`

## Questão 3
Na terceira questão, empregamos o algoritmo ID3 e armazenamos a árvore de decisão em um formato JSON 
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
Para executá-lo, é suficiente executar o script em Python, desde que a base de dados esteja armazenado no mesmo diretório com o nome `dados.csv`.  
No diretório `terceiro`, realize a execução do seguinte comando:  
* `python3 main.py`
