# glossario_ti.py
# 📖 Glossário de TI para iniciantes
# Regras de negócio incluídas

import difflib

GLOSSARIO = {
    "Python":
    "Linguagem de programação de alto nível, usada em ciência de dados, web e automação.",
    "SQL":
    "Linguagem padrão para gerenciamento de bancos de dados relacionais.",
    "Front-end":
    "Parte visual de um site ou aplicativo, com a qual o usuário interage.",
    "Back-end":
    "Parte lógica e de processamento de um sistema, que roda no servidor.",
    "GitHub":
    "Plataforma para versionamento de código e colaboração entre desenvolvedores.",
    "Algoritmo":
    "Conjunto de passos lógicos e bem definidos para resolver um problema.",
    "HTML": "Linguagem de marcação que estrutura páginas web.",
    "CSS": "Folhas de estilo que definem o visual de páginas web."
}


# ---------------- Regras de negócio ----------------
def consultar_termo(termo: str) -> str:
    termo = termo.strip().lower()

    # Regra 1: termo com pelo menos 3 caracteres
    if len(termo) < 3:
        return "⚠️ O termo deve ter pelo menos 3 caracteres."

    # Case-insensitive (não diferencia maiúsculas/minúsculas)
    for chave, definicao in GLOSSARIO.items():
        if termo == chave.lower():
            return f"✅ {chave}: {definicao}"

    # Regra 2: sugestão de termo parecido, se não encontrar
    candidatos = [t.lower() for t in GLOSSARIO.keys()]
    sugestoes = difflib.get_close_matches(termo, candidatos, n=1, cutoff=0.6)
    if sugestoes:
        termo_sugerido = next(k for k in GLOSSARIO.keys()
                              if k.lower() == sugestoes[0])
        return f"❌ Termo não encontrado. Você quis dizer **{termo_sugerido}**?"

    # Regra 3: mensagem padrão quando não há parecido
    return "❌ Termo não encontrado. Sugestão: incluir no glossário futuramente."


# ---------------- Execução Interativa ----------------
if __name__ == "__main__":
    print("=== 📖 Glossário de TI para Iniciantes ===\n")
    while True:
        termo = input("Digite um termo de TI (ou 'sair' para encerrar): ")
        if termo.lower() == "sair":
            print("Encerrando... 👋")
            break
        print(consultar_termo(termo))
        print("-" * 50)


def executar():
    print("=== 📖 Glossário de TI para Iniciantes ===\n")
    while True:
        termo = input("Digite um termo de TI (ou 'sair' para encerrar): ")
        if termo.lower() == "sair":
            print("Encerrando... 👋")
            break
        print(consultar_termo(termo))
        print("-" * 50)


if __name__ == "__main__":
    executar()
