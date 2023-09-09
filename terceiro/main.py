import math
import pandas as pd

global TARGET


def entropy(df):
    somatorio = 0
    for value in df[TARGET].unique():
        p_i = len(df[df.Risco == value]) / len(df)
        somatorio += p_i * math.log2(p_i)
    return -somatorio


def info_gain(df, colum):
    entropia_S = entropy(df)
    somatorio = 0
    for value in df[colum].unique():
        novo_S = df[df[colum] == value]
        somatorio += (len(novo_S) / len(df)) * entropy(novo_S)
    resultado = entropia_S - somatorio
    return resultado


def traverse_tree(df):
    json = dict()

    if entropy(df) == 0:
        return {TARGET: df[TARGET].unique()[0]}

    max_ig = -1e6
    select_column = str()
    for column in df.columns:
        if column == TARGET:
            continue

        curr_ig = info_gain(df, column)
        if curr_ig > max_ig:
            max_ig = curr_ig
            select_column = column

    json["pergunta"] = select_column
    json["respostas"] = list()
    for aresta in df[select_column].unique():
        filtered_df = df[df[select_column] == aresta]
        mini_json = traverse_tree(filtered_df)
        json["respostas"].append({aresta: mini_json})
    return json


def perguntar(json):
    if TARGET in json:
        print(json[TARGET])
        return
    print(f"Qual o valor de {json['pergunta']}")
    possiveis_respostas = [list(x.keys())[0] for x in json['respostas']]
    for idx, resposta in enumerate(possiveis_respostas):
        print(f"({idx + 1}) {resposta}")
    ans = int(input())
    resposta = possiveis_respostas[ans - 1]
    mini_json = json["respostas"][ans - 1][resposta]
    perguntar(mini_json)


def main():
    global TARGET
    TARGET = "Risco"
    df = pd.read_csv("dados.csv")
    res = traverse_tree(df)
    perguntar(res)


if __name__ == '__main__':
    main()
