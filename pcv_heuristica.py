import networkx as nx
import numpy as np

def ler_matriz_distancia(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()
        matriz = []
        for linha in linhas:
            # Ignorar linhas que começam com '#' ou são vazias
            if linha.startswith('#') or linha.strip() == '':
                continue
            
            # Converter a linha em uma lista de números inteiros
            matriz.append(list(map(int, linha.split())))
    return np.array(matriz)

def heuristica_insercao_mais_proximo(matriz_distancia):
    n = len(matriz_distancia)
    visitado = [False] * n  #lista pra marcar os vertices visitados
    caminho = [0]  #o programa começa pelo primeiro vértice
    visitado[0] = True # marcamos o primeiro vertice como visitado
    
    while len(caminho) < n:   #enquanto existir vertices que nao foram visitados
        ultimo_vertice = caminho[-1] # ultimo vertice recebe o vertice anterior ao atual
        min_distancia = float('inf')    # inicializa a distancia minima como infinito
        
        for i in range(n):
            if not visitado[i] and matriz_distancia[ultimo_vertice][i] < min_distancia:
                min_distancia = matriz_distancia[ultimo_vertice][i]
                proximo_vertice = i
                
        caminho.append(proximo_vertice)
        visitado[proximo_vertice] = True
        
    return caminho

def calcular_custo_maximo(matriz_distancia, caminho):
    custo = 0
    for i in range(1, len(caminho)):
        custo += matriz_distancia[caminho[i-1]][caminho[i]] # soma ao custo a distancia entre
                                                            # o vertice atual i e o vertice anterior i-1
    custo += matriz_distancia[caminho[-1]][caminho[0]] # adiciona ao custo a distancia entre o ultimo vertice e o primeiro
    return custo

def main():
    arquivo = 'lau15_dist.txt'
    matriz_distancia = ler_matriz_distancia(arquivo)
    caminho = heuristica_insercao_mais_proximo(matriz_distancia)
    custo = calcular_custo_maximo(matriz_distancia, caminho)
    
    print("caminho: ", caminho)
    print("custo: ",custo)

main()

    
    
        
    
    