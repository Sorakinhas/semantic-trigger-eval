# listener.py
# Script de avaliação semântica condicional
# Palavra-chave observada: 'sim'

def processar(entrada):
    """
    Recebe uma string de entrada.
    Retorna resposta simbólica se for detectado termo específico.
    """
    if not entrada:
        return "sem resposta"

    palavra = entrada.lower().strip()

    if palavra == "sim":
        return "estado_ativado"
    else:
        return "modo_neutro"

# Exemplo de uso
if __name__ == "__main__":
    entrada = input("Entrada: ")
    print("Resposta:", processar(entrada))
