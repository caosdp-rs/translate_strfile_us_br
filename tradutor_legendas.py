import os
import re
from googletrans import Translator
import time
import random
from tqdm import tqdm

def traduzir_srt(arquivo_entrada, arquivo_saida):
    if os.path.exists(arquivo_saida):
        print(f"Arquivo de saída '{arquivo_saida}' já existe. Pulando tradução.")
        return
    print("entrada:" + arquivo_entrada)
    print("saida"+arquivo_saida)
    with open(arquivo_entrada, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
    total_linhas = len(linhas)
    linhas_processadas = 0

    translator = Translator()
    linhas_traduzidas = []

    with tqdm(total=total_linhas, desc="Traduzindo"+arquivo_entrada, unit="linha") as pbar:
        for indice, linha in enumerate(linhas):
            if not linha.strip():
                linhas_traduzidas.append('\n')
            elif '-->' in linha:
                linhas_traduzidas.append(linha)
            else:
                traducao = translator.translate(linha, src='en', dest='pt')
                linhas_traduzidas.append(traducao.text + '\n')

            pbar.update(1)

            # Adiciona um atraso aleatório entre 1 e 2 segundos entre as traduções
            atraso_aleatorio = random.uniform(1, 2)
            time.sleep(atraso_aleatorio)

    print("\nTradução concluída.")

    with open(arquivo_saida, 'w', encoding='utf-8') as file:
        file.writelines(linhas_traduzidas)


def traduzir_todos_arquivos_srt(diretorio_entrada, diretorio_saida):
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    for arquivo in os.listdir(diretorio_entrada):
        if arquivo.endswith(".srt"):
            caminho_entrada = os.path.join(diretorio_entrada, arquivo)

            # Alteração no nome do arquivo de saída
            nome_arquivo, extensao = os.path.splitext(arquivo)
            nome_arquivo = re.sub(r'en_US', 'pt_BR', nome_arquivo)
            caminho_saida = os.path.join(diretorio_saida, nome_arquivo + extensao)
            traduzir_srt(caminho_entrada, caminho_saida)


if __name__ == "__main__":
    print("iniciando")
    diretorio_entrada = "C:\\Users\\c4osx\\Videos\\TubeDigger"
    diretorio_saida = "C:\\Users\\c4osx\\Videos\\TubeDigger"

    traduzir_todos_arquivos_srt(diretorio_entrada, diretorio_saida)
