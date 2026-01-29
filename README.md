# Subdomain-Enumerator
DNS Subdomain Enumeration Tool (Educational Project)

This tool was developed to understand how DNS-based subdomain enumeration works using Python and the dnspython library, including how wildcard DNS can affect reconnaissance results.

Features:

Wordlist-based subdomain brute force enumeration

DNS A record resolution

Automatic wildcard DNS detection

False positive filtering caused by wildcard DNS

Identification of valid and reachable subdomains


What this project demonstrates:

DNS reconnaissance techniques used during the recon phase

Understanding of DNS resolution and wildcard behavior

Attack surface mapping through subdomain discovery

Why wildcard DNS can break naive enumeration tools


How it works:
A random subdomain is generated to test wildcard DNS behavior
If the random subdomain resolves, wildcard DNS is detected
During brute force, subdomains resolving to wildcard IPs are ignored
Only real and unique subdomains are displayed

Limitations:
Resolves only A records
No multi-threading or performance optimization
Designed for learning purposes, not large-scale scans

Requirements:
Python 3.x
dnspython library

Why I built this:
I wanted to understand how tools like Sublist3r, Amass, and Assetfinder work internally, instead of using them as black boxes.
This project helped me learn how DNS resolution, brute force enumeration, and wildcard filtering are implemented at a low level.

Disclaimer:
Educational use only.
Developed and tested exclusively in authorized lab environments.



xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



Ferramenta de Enumeração de Subdomínios DNS (Projeto Educacional)

Esta ferramenta foi desenvolvida com o objetivo de entender, na prática, como funciona a enumeração de subdomínios via DNS utilizando Python e a biblioteca dnspython, incluindo o impacto do wildcard DNS durante a fase de reconhecimento.

Funcionalidades:
Enumeração de subdomínios por força bruta utilizando wordlist
Resolução de registros DNS do tipo A
Detecção automática de wildcard DNS
Filtragem de falsos positivos causados por wildcard DNS
Identificação de subdomínios válidos e acessíveis

O Que Este Projeto Demonstra:
Técnicas de reconhecimento DNS usadas na fase de recon
Funcionamento da resolução DNS e do wildcard DNS
Mapeamento da superfície de ataque através de subdomínios
Por que ferramentas ingênuas falham quando existe wildcard DNS

Como Funciona:
Um subdomínio aleatório é gerado para testar a presença de wildcard DNS
Caso o subdomínio aleatório resolva, o wildcard é identificado
Durante o brute force, subdomínios que retornam IPs de wildcard são ignorados
Apenas subdomínios reais e únicos são exibidos no resultado final

Requisitos:
Python 3.x
Biblioteca dnspython

Limitações:
Resolve apenas registros DNS do tipo A
Não possui otimizações de desempenho (multi-threading)
Desenvolvida para fins educacionais e aprendizado

Por Que Eu Desenvolvi Esta Ferramenta:
Desenvolvi este projeto para entender como ferramentas profissionais como Sublist3r, Amass e Assetfinder funcionam internamente, em vez de utilizá-las apenas como “caixas-pretas”.
O foco foi aprender como ocorre a enumeração DNS, a detecção de wildcard e a filtragem de falsos positivos em um nível mais baixo.

Aviso Legal:
Este projeto é destinado exclusivamente para fins educacionais.
Utilize apenas em sistemas próprios ou com autorização explícita
O autor não se responsabiliza por uso indevido
Testes realizados apenas em ambientes de laboratório controlados
