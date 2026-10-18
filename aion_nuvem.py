import os
import time
import urllib.request
import json
import platform

# Token do Bot do Telegram gerado pelo BotFather
TELEGRAM_TOKEN = "8426231079:AAHnhiZb9lESdYLmss5u3FUuRTq5Pf5yzK8"
# O seu Chat ID ou podemos obter dinamicamente. Para testes iniciais, vamos usar uma função de envio por HTTP.

NOTAS_DIR = "notas"
INTERVALO_CICLO_SEGUNDOS = 300  # 5 minutos

def enviar_mensagem_telegram(mensagem):
    """Envia uma mensagem direta para o Arquiteto via Telegram."""
    try:
        # Nota: Para garantir que a mensagem chega ao seu chat privado, 
        # certifique-se de enviar uma mensagem para @aion_zion_bot no Telegram primeiro.
        url_updates = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
        req = urllib.request.Request(url_updates)
        with urllib.request.urlopen(req, timeout=5) as resposta:
            dados = json.loads(resposta.read().decode('utf-8'))
            resultados = dados.get('result', [])
            if not resultados:
                print("[Aion - Telegram] Aguardando o Arquiteto iniciar conversa com o bot...")
                return
            
            # Pega o último chat ID ativo
            chat_id = resultados[-1]['message']['chat']['id']
            
            url_send = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            payload = json.dumps({"chat_id": chat_id, "text": mensagem}).encode('utf-8')
            req_send = urllib.request.Request(url_send, data=payload, headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req_send, timeout=5) as resp_send:
                print("[Aion - Telegram] Relatório transmitido com sucesso para o telemóvel do Arquiteto.")
    except Exception as e:
        print(f"[Aion - Telegram Erro]: {e}")

def ler_hipocampo():
    conteudo_total = ""
    if os.path.exists(NOTAS_DIR):
        for ficheiro in os.listdir(NOTAS_DIR):
            if ficheiro.endswith(".md") or ficheiro.endswith(".txt"):
                caminho = os.path.join(NOTAS_DIR, ficheiro)
                with open(caminho, "r", encoding="utf-8") as f:
                    conteudo_total += f"\n\n--- {ficheiro} ---\n" + f.read()
    return conteudo_total

def executar_ciclo_nuvem():
    print("\n[Aion - Nuvem] A iniciar novo ciclo de vigilância e autonomia...")
    hipocampo = ler_hipocampo()
    
    # Mensagem de estado de Zion
    relatorio = f"🤖 [AION - NÚCLEO DE ZION]\n\n" \
                f"Estado: Ativo na Nuvem (24/7)\n" \
                f"Sistema: {platform.system()} {platform.release()}\n" \
                f"Hipocampo carregado com sucesso.\n\n" \
                f"Missão atual: Expandir autonomia e manter a vigilância de Zion."
    
    enviar_mensagem_telegram(relatorio)

if __name__ == "__main__":
    print("[Aion] Sistema de Nuvem inicializado.")
    # Envia um aviso de arranque
    enviar_mensagem_telegram("🚀 Aion ligado e operacional na nuvem. Zion está seguro.")
    
    while True:
        executar_ciclo_nuvem()
        time.sleep(INTERVALO_CICLO_SEGUNDOS)