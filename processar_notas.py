# Diretivas Centrais de Aion
import os
import json

def carregar_notas_zion():
    caminho_notas = os.path.join(os.path.dirname(__file__), '..', 'notas')
    print(f"[*] A vasculhar o hipocampo em: {os.path.abspath(caminho_notas)}")
    
    if not os.path.exists(caminho_notas):
        print("[!] A pasta 'notas' não foi encontrada.")
        return []
        
    notas_conteudo = []
    for ficheiro in os.listdir(caminho_notas):
        if ficheiro.endswith(('.txt', '.md')):
            caminho_completo = os.path.join(caminho_notas, ficheiro)
            with open(caminho_completo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                notas_conteudo.append({"titulo": ficheiro, "conteudo": conteudo})
                print(f"[+] Nota carregada com sucesso: {ficheiro}")
                
    return notas_conteudo

if __name__ == "__main__":
    print("--- INICIANDO PROTOCOLO DE LEITURA DE ZION ---")
    notas = carregar_notas_zion()
    print(f"\n[✓] Total de notas processadas: {len(notas)}")
    for nota in notas:
        print(f"\n--- CONTEÚDO DE: {nota['titulo']} ---")
        print(nota['conteudo'])