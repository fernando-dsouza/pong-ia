# Pong IA
Este projeto consiste no desenvolvimento do jogo Pong, controlado por uma rede neural treinada com algoritmos de 
aprendizado de máquina. 
O objetivo é criar uma inteligência artificial capaz de jogar o jogo de forma autônoma, sem intervenção humana.

O jogo foi desenvolvido em Python, utilizando a biblioteca Pygame para renderizar as imagens. 
A rede neural foi desenvolvida para ser utilizada em conjunto com um algoritmo genético, que gera os parâmetros 
iniciais da rede e realiza a seleção artificial dos melhores indivíduos de cada geração, bem como o cruzamento e a 
mutação das populações das demais gerações.

A rede neural possui três entradas: posição da bola, altura da bola, posição da raquete. 
Na camada oculta, há dez neurônios e duas saídas para controlar a raquete. A rede tem 62 parâmetros e função de 
ativação utilizada foi a ReLU (Rectified Linear Unit), que é uma função de ativação não linear que permite que padrões 
complexos nos dados sejam aprendidos.


# Instalação 
Para executar o jogo Pong IA, siga as instruções abaixo:

1. Tenha o Python instalada em sua máquina, caso não tenha veja no site https://www.python.org/.
2. Abra o terminal na pasta do projeto e instale a biblioteca Pygame digitando o seguinte código no terminal:
    ```bash
    pip install pygame
    ```
3. Execute o arquivo main.py no terminal:
    ```bash
    python main.py
    ```

# Preview
<img alt="preview" src="https://user-images.githubusercontent.com/56095974/227356314-ebeed46c-89a7-4aa8-8a2c-3d4d3837579e.png" width="512">
