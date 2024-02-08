import ntplib

# Abrir o arquivo contendo os endereços IP
with open('ips.txt', 'r') as file:
    # Iterar sobre cada linha do arquivo
    for line in file:
        # Remover espaços em branco e quebras de linha
        ip = line.strip()
        
        try:
            # Criar um cliente NTP
            client = ntplib.NTPClient()

            # Fazer uma requisição para o servidor NTP
            response = client.request(ip)

            # Exibir a resposta
            print(f"Resposta do servidor {ip}: {response.tx_time}")

        except ntplib.NTPException as e:
            print(f"Erro ao fazer a requisição para o servidor {ip}: {e}")