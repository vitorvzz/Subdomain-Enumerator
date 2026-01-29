import dns.resolver
import random
import string

# Configurações
alvo = "bancocn.com"
wordlist = "/home/kali/wordlist.txt"

resolver = dns.resolver.Resolver()

# -------------------------
# FUNÇÃO: detectar wildcard
# -------------------------
def tem_wildcard_dns(alvo):
    random_sub = ''.join(random.choices(string.ascii_lowercase, k=15))
    teste = f"{random_sub}.{alvo}"

    try:
        resposta = resolver.resolve(teste, "A")
        ips = [ip.to_text() for ip in resposta]
        print(f"[!] Wildcard DNS detectado: {ips}")
        return ips
    except:
        print("[+] Nenhum wildcard DNS detectado")
        return None


# -------------------------
# MAIN
# -------------------------
wildcard_ips = tem_wildcard_dns(alvo)

arquivo = open(wordlist, "r")
subdominios = arquivo.read().splitlines()

print("\n[+] Iniciando brute force de subdomínios...\n")

for subdominio in subdominios:
    sub_alvo = f"{subdominio}.{alvo}"

    try:
        resposta = resolver.resolve(sub_alvo, "A")
        ips = [ip.to_text() for ip in resposta]

        # Remove falso positivo de wildcard
        if wildcard_ips and ips == wildcard_ips:
            continue

        print(f"[+] {sub_alvo} -> {ips}")

    except:
        pass
