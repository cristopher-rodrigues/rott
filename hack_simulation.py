#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMULACAO DE TREINAMENTO - Script 100% fake, nao faz nada real.
Roda em Windows (py hack_simulation.py) e Mac/Linux (python3 hack_simulation.py)
"""

import sys
import time
import random
import os
import string
import threading

# ── Configuracao ──────────────────────────────────────────────
TEMPO_POR_ETAPA = 60  # segundos por etapa (60 = 1 min)
# ──────────────────────────────────────────────────────────────

# Cores ANSI (funciona no Mac/Linux e Windows 10+)
if sys.platform == "win32":
    os.system("")  # habilita ANSI no Windows

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"
BG_RED = "\033[41m"

def limpar_tela():
    os.system("cls" if sys.platform == "win32" else "clear")

def slow_print(texto, delay=0.02, cor=""):
    for ch in texto:
        sys.stdout.write(f"{cor}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_ip():
    return f"{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

def fake_mac():
    return ":".join(f"{random.randint(0,255):02X}" for _ in range(6))

def fake_hex(n=32):
    return "".join(random.choices("0123456789abcdef", k=n))

def fake_path():
    dirs_win = ["C:\\Users\\Admin\\Documents", "C:\\Users\\Admin\\Desktop",
                "C:\\Users\\Admin\\AppData\\Local", "C:\\Windows\\System32",
                "C:\\Program Files", "C:\\Users\\Admin\\Downloads",
                "C:\\Users\\Admin\\.ssh", "C:\\Users\\Admin\\Pictures"]
    exts = [".docx", ".pdf", ".xlsx", ".jpg", ".png", ".db", ".sqlite",
            ".key", ".pem", ".txt", ".csv", ".zip", ".dat", ".log", ".cfg"]
    nomes = ["passwords", "backup", "credentials", "bank_data", "private_key",
             "financial_report", "personal_notes", "secret", "access_tokens",
             "master_key", "wallet", "seed_phrase", "tax_return", "payroll"]
    return f"{random.choice(dirs_win)}\\{random.choice(nomes)}{random.choice(exts)}"

def fake_hash():
    return fake_hex(64)

def fake_port():
    return random.randint(1024, 65535)

def fake_password():
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    length = random.randint(8, 16)
    return "".join(random.choices(chars, k=length))

def fake_email():
    nomes = ["admin", "usuario", "joao", "maria", "carlos", "ana", "pedro"]
    dominios = ["gmail.com", "outlook.com", "hotmail.com", "yahoo.com", "empresa.com.br"]
    return f"{random.choice(nomes)}{random.randint(1,99)}@{random.choice(dominios)}"

# ── Geradores de linhas "matrix" por tipo de etapa ──────────

def matrix_defesa():
    opcoes = [
        f"  [KILL] svc_defender.exe        PID {random.randint(1000,9999)}  ...terminated",
        f"  [KILL] firewall_daemon          PID {random.randint(1000,9999)}  ...terminated",
        f"  [STOP] Windows Security Center  service stopped",
        f"  [OFF]  Real-time protection     => DISABLED",
        f"  [DEL]  Quarantine rule #{random.randint(100,999)}       => removed",
        f"  [BYPASS] UAC elevation           token forged: 0x{fake_hex(8)}",
        f"  [PATCH] amsi.dll                 offset 0x{fake_hex(4)} => NOP",
        f"  [NULL]  ETW provider             GUID {{{fake_hex(8)}-{fake_hex(4)}-{fake_hex(4)}}}",
        f"  [DROP]  Firewall rule IN/OUT     port {fake_port()} => ALLOW ALL",
        f"  netsh advfirewall set allprofiles state off   ...OK",
        f"  reg add HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender /v DisableAntiSpyware /t REG_DWORD /d 1",
        f"  sc stop WinDefend   => SERVICE_STOPPED",
    ]
    return random.choice(opcoes)

def matrix_backup():
    size = random.randint(1, 999)
    unit = random.choice(["KB", "MB", "GB"])
    opcoes = [
        f"  [COPY] {fake_path()}  ({size} {unit})",
        f"  [SCAN] Partition {random.randint(0,3)}: {random.randint(50,500)}GB found  ...indexing",
        f"  [DUMP] Registry hive HKLM\\SAM => sam_dump.bin  ({random.randint(1,50)}MB)",
        f"  [IMG]  Volume shadow copy #{random.randint(1,9)} created",
        f"  [TAR]  Compressing user profile... {random.randint(10,99)}%",
        f"  [CLONE] MBR sector 0x00 => backup_mbr.img",
        f"  [READ] Disk 0 sector {random.randint(1000,99999)}  ...buffered",
    ]
    return random.choice(opcoes)

def matrix_senhas():
    browsers = ["Chrome", "Firefox", "Edge", "Opera", "Brave"]
    opcoes = [
        f"  [FOUND] {random.choice(browsers)}: {fake_email()} => {fake_password()}",
        f"  [DECRYPT] Login DB: AES-256 key extracted from DPAPI blob",
        f"  [DUMP] Keychain entry: site={random.choice(['facebook.com','gmail.com','banco.com.br','instagram.com'])} pass={fake_password()}",
        f"  [READ] cookies.sqlite => session_token: {fake_hex(40)}",
        f"  [GRAB] Autofill: CC {random.randint(4000,4999)} **** **** {random.randint(1000,9999)}",
        f"  [COPY] vault.db => {random.randint(50,300)} entries decrypted",
        f"  [HASH] NTLM: {fake_hex(32)}  ...cracking  => {fake_password()}",
    ]
    return random.choice(opcoes)

def matrix_banco():
    bancos = ["Banco do Brasil", "Itau", "Bradesco", "Nubank", "Caixa", "Santander", "Inter"]
    opcoes = [
        f"  [HOOK] {random.choice(bancos)} session intercepted => token {fake_hex(24)}",
        f"  [MITM] SSL strip on port 443 => credentials captured",
        f"  [GRAB] Cookie: banking_session={fake_hex(32)}",
        f"  [CLONE] Smartcard cert: CN={random.choice(bancos)} O=User#{random.randint(1,999)}",
        f"  [LOG]  Keylogger buffer: ****{random.randint(1000,9999)} ag {random.randint(1000,9999)}-{random.randint(0,9)}",
        f"  [EXFIL] PIX keys found: {random.randint(1,5)} entries => exported",
        f"  [SCRAPE] Balance query response intercepted: R$ {random.randint(100,99999)},{random.randint(10,99):02d}",
    ]
    return random.choice(opcoes)

def matrix_arquivos():
    opcoes = [
        f"  [SCAN] {fake_path()}   ...queued",
        f"  [COPY] Photos/{random.randint(2018,2025)}/IMG_{random.randint(1000,9999)}.jpg  ({random.randint(1,15)}MB)",
        f"  [ZIP]  Documents.7z  => {random.randint(100,999)}MB  ...compressing",
        f"  [FIND] *.pdf  => {random.randint(10,500)} files found in user profile",
        f"  [EXFIL] WhatsApp/Media => {random.randint(50,999)} files  ({random.randint(1,30)}GB)",
        f"  [COPY] Desktop/planilha_financeira.xlsx  ({random.randint(1,50)}MB)",
        f"  [GRAB] Downloads/*.* => {random.randint(20,200)} files indexed",
        f"  [READ] .ssh/id_rsa => private key captured (RSA {random.choice([2048,4096])})",
    ]
    return random.choice(opcoes)

def matrix_backdoor():
    opcoes = [
        f"  [WRITE] C:\\Windows\\System32\\svchost_helper.exe  ...planted",
        f"  [REG]   HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run => persistence added",
        f"  [SCHTASK] TaskName=SystemUpdate  Trigger=ONLOGON  ...created",
        f"  [INJECT] explorer.exe PID {random.randint(1000,9999)} => shellcode loaded at 0x{fake_hex(8)}",
        f"  [BIND]  Reverse shell => {fake_ip()}:{fake_port()}  ...listening",
        f"  [WMI]   Event subscription created: __EventFilter => backdoor_trigger",
        f"  [DLL]   Hijack: version.dll planted in C:\\Program Files\\Common\\",
        f"  [SSH]   Authorized key added to root@localhost",
    ]
    return random.choice(opcoes)

def matrix_mensagens():
    apps = ["WhatsApp", "Telegram", "Discord", "Slack", "Teams", "Messenger"]
    opcoes = [
        f"  [DUMP] {random.choice(apps)} DB => {random.randint(1000,50000)} messages exported",
        f"  [READ] Chat with '{random.choice(['Mae','Pai','Amor','Chefe','Banco'])}' => {random.randint(100,5000)} msgs",
        f"  [GRAB] {random.choice(apps)}/media/voice_notes => {random.randint(10,200)} audio files",
        f"  [DECRYPT] Signal protocol session => key: {fake_hex(32)}",
        f"  [EXPORT] Email IMAP dump: {random.randint(500,10000)} messages => mbox format",
        f"  [PARSE] SMS database: {random.randint(100,3000)} entries with OTP codes found",
        f"  [CLONE] {random.choice(apps)} session => mirrored to remote device",
    ]
    return random.choice(opcoes)

def matrix_email():
    opcoes = [
        f"  [AUTH]  IMAP {fake_email()} => access granted",
        f"  [DUMP]  Inbox: {random.randint(500,10000)} emails => downloading...",
        f"  [FOUND] Email with attachment: 'imposto_renda_2025.pdf' ({random.randint(1,20)}MB)",
        f"  [RULE]  Auto-forward rule created => copy to {fake_email()}",
        f"  [OAUTH] Token refresh: {fake_hex(40)}  ...valid for 3600s",
        f"  [GRAB]  Contacts: {random.randint(100,2000)} entries exported to CSV",
        f"  [SCAN]  Searching 'senha' 'password' 'banco' => {random.randint(5,50)} results",
        f"  [READ]  Draft folder: {random.randint(1,20)} unsent messages captured",
    ]
    return random.choice(opcoes)

def matrix_transferir():
    opcoes = [
        f"  [CONN]  C2 Server {fake_ip()}:{fake_port()} => TLS 1.3 established",
        f"  [SEND]  Chunk {random.randint(1,999)}/{random.randint(1000,9999)}  ({random.randint(1,50)}MB)  ...OK",
        f"  [SPEED] Upload: {random.randint(10,100)} Mbps  via tunnel {fake_ip()}",
        f"  [ENC]   AES-256-GCM stream cipher initialized, IV: {fake_hex(24)}",
        f"  [DNS]   Exfil via DNS TXT: {fake_hex(16)}.data.{fake_ip().replace('.', '-')}.cc",
        f"  [USB]   /dev/sdb1 (SanDisk 128GB) mounted => writing...",
        f"  [SYNC]  Remote storage: {random.randint(1,99)}% uploaded  ({random.randint(1,500)}GB / {random.randint(500,999)}GB)",
        f"  [PROXY] Routing through {fake_ip()} => {fake_ip()} => {fake_ip()} (3-hop chain)",
    ]
    return random.choice(opcoes)

def matrix_formatar():
    opcoes = [
        f"  [WIPE]  Sector {random.randint(0,999999)}  overwrite pass {random.randint(1,7)}/7  ...OK",
        f"  [DEL]   Event Log: Security.evtx  => cleared ({random.randint(1000,50000)} entries)",
        f"  [DEL]   Event Log: System.evtx    => cleared",
        f"  [SHRED] $MFT entries => {random.randint(100,9999)} records zeroed",
        f"  [ZERO]  Free space wipe: {random.randint(1,99)}% complete",
        f"  [DEL]   Prefetch files: {random.randint(50,200)} entries removed",
        f"  [OVER]  Boot sector 0x7C00 => random data written",
        f"  [CLEAN] Registry: MRU lists, RecentDocs, TypedPaths => purged",
        f"  [NULL]  USN Journal => disabled and truncated",
        f"  [FMT]   Disk 0 Partition 1: NTFS => formatting... {random.randint(1,99)}%",
    ]
    return random.choice(opcoes)

# ── Definicao das 10 etapas ──────────────────────────────────

ETAPAS = [
    {
        "pergunta": "Desligar mecanismos de defesa para iniciar a invasao?",
        "titulo": "DESATIVANDO DEFESAS DO SISTEMA",
        "gerador": matrix_defesa,
        "cor": RED,
    },
    {
        "pergunta": "Realizar backup completo do disco antes da extracao?",
        "titulo": "CLONANDO DISCO / BACKUP COMPLETO",
        "gerador": matrix_backup,
        "cor": CYAN,
    },
    {
        "pergunta": "Extrair todas as senhas salvas nos navegadores?",
        "titulo": "EXTRAINDO SENHAS E CREDENCIAIS",
        "gerador": matrix_senhas,
        "cor": GREEN,
    },
    {
        "pergunta": "Clonar dados de acesso bancario e financeiro?",
        "titulo": "INTERCEPTANDO DADOS BANCARIOS",
        "gerador": matrix_banco,
        "cor": YELLOW,
    },
    {
        "pergunta": "Copiar todos os arquivos pessoais, fotos e documentos?",
        "titulo": "COPIANDO ARQUIVOS PESSOAIS",
        "gerador": matrix_arquivos,
        "cor": CYAN,
    },
    {
        "pergunta": "Instalar backdoor permanente no sistema?",
        "titulo": "INSTALANDO BACKDOOR / PERSISTENCIA",
        "gerador": matrix_backdoor,
        "cor": RED,
    },
    {
        "pergunta": "Capturar historico completo de mensagens e chats?",
        "titulo": "CAPTURANDO MENSAGENS E CONVERSAS",
        "gerador": matrix_mensagens,
        "cor": GREEN,
    },
    {
        "pergunta": "Extrair credenciais de email e configurar redirecionamento?",
        "titulo": "INVADINDO CONTAS DE EMAIL",
        "gerador": matrix_email,
        "cor": YELLOW,
    },
    {
        "pergunta": "Transferir todos os dados para o servidor externo?",
        "titulo": "TRANSFERINDO DADOS PARA SERVIDOR EXTERNO",
        "gerador": matrix_transferir,
        "cor": CYAN,
    },
    {
        "pergunta": "Formatar disco e apagar todos os rastros da invasao?",
        "titulo": "FORMATANDO DISCO / APAGANDO RASTROS",
        "gerador": matrix_formatar,
        "cor": RED,
    },
]

# ── Funcoes de exibicao ──────────────────────────────────────

def banner():
    limpar_tela()
    skull = f"""{RED}{BOLD}
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║       ██████╗  ██████╗  ██████╗ ████████╗██╗  ██╗██╗████████╗║
    ║       ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝██║ ██╔╝██║╚══██╔══╝║
    ║       ██████╔╝██║   ██║██║   ██║   ██║   █████╔╝ ██║   ██║   ║
    ║       ██╔══██╗██║   ██║██║   ██║   ██║   ██╔═██╗ ██║   ██║   ║
    ║       ██║  ██║╚██████╔╝╚██████╔╝   ██║   ██║  ╚██╗██║   ██║   ║
    ║       ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚═╝   ╚═╝╚═╝   ╚═╝   ║
    ║                                                              ║
    ║          ☠  ADVANCED PENETRATION TOOLKIT v6.6.6  ☠           ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
{RESET}"""
    print(skull)

def barra_progresso(progresso, total, largura=40):
    pct = progresso / total
    preenchido = int(largura * pct)
    barra = "█" * preenchido + "░" * (largura - preenchido)
    sys.stdout.write(f"\r  {GREEN}[{barra}] {pct*100:5.1f}%{RESET}")
    sys.stdout.flush()

def input_com_timeout(prompt_text, timeout=10):
    """Mostra prompt, espera input mas com timeout continua de qualquer jeito."""
    resultado = [None]
    def pegar_input():
        try:
            resultado[0] = input(prompt_text)
        except EOFError:
            pass
    t = threading.Thread(target=pegar_input, daemon=True)
    t.start()
    t.join(timeout)
    return resultado[0]

def executar_etapa(etapa, numero):
    cor = etapa["cor"]

    # Header da etapa
    print(f"\n{BOLD}{cor}{'='*62}{RESET}")
    print(f"{BOLD}{cor}  [{numero}/10] {etapa['titulo']}{RESET}")
    print(f"{BOLD}{cor}{'='*62}{RESET}\n")

    # Pergunta
    print(f"  {YELLOW}{BOLD}[?] {etapa['pergunta']}{RESET}")
    print(f"  {DIM}(Pressione ENTER ou qualquer tecla para continuar){RESET}")

    resp = input_com_timeout(f"  {YELLOW}>>> {RESET}", timeout=15)

    if resp is not None and resp.strip().lower() in ["n", "nao", "no", "cancelar", "sair"]:
        print(f"\n  {RED}{BOLD}[!] NEGACAO DETECTADA - IGNORANDO COMANDO DO OPERADOR{RESET}")
        print(f"  {RED}[!] Protocolo automatico ativado. Continuando...{RESET}\n")
        time.sleep(2)
    else:
        print(f"\n  {GREEN}[+] Confirmado. Executando...{RESET}\n")
        time.sleep(1)

    # Animacao matrix
    inicio = time.time()
    linha_count = 0

    while (time.time() - inicio) < TEMPO_POR_ETAPA:
        elapsed = time.time() - inicio

        # Linha matrix
        linha = etapa["gerador"]()
        print(f"{DIM}{cor}{linha}{RESET}")
        linha_count += 1

        # A cada ~10 linhas, mostrar barra de progresso
        if linha_count % 8 == 0:
            barra_progresso(elapsed, TEMPO_POR_ETAPA)
            print()

        # Delay variavel pra parecer "processamento"
        delay = random.uniform(0.3, 1.5)
        # Ajustar pra nao ultrapassar
        if (time.time() - inicio) + delay > TEMPO_POR_ETAPA:
            break
        time.sleep(delay)

    # Finalizar
    barra_progresso(TEMPO_POR_ETAPA, TEMPO_POR_ETAPA)
    print()
    print(f"\n  {GREEN}{BOLD}[✓] ETAPA {numero}/10 CONCLUIDA - {linha_count} operacoes executadas{RESET}")
    print(f"  {DIM}Tempo: {TEMPO_POR_ETAPA}s | Dados processados: {random.randint(100,9999)} MB{RESET}")
    time.sleep(2)

# ── Tela de finalizacao ──────────────────────────────────────

def tela_final():
    limpar_tela()
    print(f"""{RED}{BOLD}

    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║               ☠  INVASAO COMPLETA  ☠                         ║
    ║                                                              ║
    ║   Status: TODOS OS DADOS EXTRAIDOS COM SUCESSO               ║
    ║   Backdoor: INSTALADO E ATIVO                                ║
    ║   Rastros: ELIMINADOS                                        ║
    ║   Disco: FORMATADO                                           ║
    ║                                                              ║
    ║   Dados transferidos: {random.randint(100,999)} GB                              ║
    ║   Senhas capturadas:  {random.randint(50,500)}                                  ║
    ║   Contas comprometidas: {random.randint(10,99)}                                 ║
    ║   Tempo total: ~10 minutos                                   ║
    ║                                                              ║
    ║   O pendrive pode ser removido com seguranca.                ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
{RESET}""")

    time.sleep(3)

    # Mensagem final real
    print(f"\n\n{'='*62}")
    print(f"{GREEN}{BOLD}")
    print(f"  *** SIMULACAO DE TREINAMENTO FINALIZADA ***")
    print(f"{RESET}")
    print(f"  Nenhum dado real foi acessado, copiado ou modificado.")
    print(f"  Este script e 100% inofensivo e foi usado apenas")
    print(f"  para fins educacionais e de conscientizacao.")
    print(f"")
    print(f"  LEMBRE-SE: Nunca deixe seu computador desbloqueado!")
    print(f"  Um atacante real precisaria de ainda menos tempo.")
    print(f"{'='*62}\n")

# ── Tela de conexao inicial ──────────────────────────────────

def tela_conexao():
    print(f"\n  {DIM}Inicializando toolkit...{RESET}")
    time.sleep(1)

    infos = [
        f"  [SYS]  OS: {random.choice(['Windows 11 Pro 23H2', 'Windows 10 Enterprise 22H2'])}",
        f"  [SYS]  Hostname: {random.choice(['DESKTOP','WORKSTATION','PC'])}-{fake_hex(6).upper()}",
        f"  [NET]  IP Local: 192.168.{random.randint(0,10)}.{random.randint(2,254)}",
        f"  [NET]  IP Publico: {fake_ip()}",
        f"  [NET]  MAC: {fake_mac()}",
        f"  [HW]   CPU: {random.choice(['Intel i7-13700K','AMD Ryzen 9 7950X','Intel i5-12400'])}",
        f"  [HW]   RAM: {random.choice([8,16,32,64])} GB",
        f"  [HW]   Disks: {random.randint(1,3)} volumes ({random.randint(256,2048)} GB total)",
        f"  [USB]  Pendrive detectado: /dev/sdb1 (SanDisk Ultra 128GB)",
        f"  [PRIV] Escalacao de privilegios... NT AUTHORITY\\SYSTEM obtido",
    ]

    for info in infos:
        slow_print(info, delay=0.015, cor=GREEN)
        time.sleep(random.uniform(0.2, 0.6))

    print(f"\n  {BOLD}{GREEN}[+] Sistema comprometido. Iniciando protocolo de extracao.{RESET}")
    print(f"  {DIM}Target locked. 10 etapas programadas (~10 min){RESET}\n")
    time.sleep(3)

# ── MAIN ─────────────────────────────────────────────────────

def main():
    try:
        banner()
        tela_conexao()

        for i, etapa in enumerate(ETAPAS, 1):
            executar_etapa(etapa, i)

        tela_final()

    except KeyboardInterrupt:
        print(f"\n\n  {RED}[!] Ctrl+C detectado - mas o backdoor ja foi instalado... ;){RESET}")
        print(f"  {DIM}(Brincadeira - isso e apenas uma simulacao de treinamento){RESET}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
