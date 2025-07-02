
import requests
from datetime import datetime, timedelta

def estrategia_2(branco_info, anterior, posterior):
    """
    Estratégia 2: Soma número anterior + posterior + minuto do branco.
    A soma resultante substitui o minuto original, mantendo a hora.
    """
    minuto_branco = branco_info['hora'].minute
    soma = anterior + posterior + minuto_branco

    # Ajuste de hora/minuto caso passe de 59
    nova_hora = branco_info['hora'].hour + (soma // 60)
    novo_minuto = soma % 60

    proximo_horario = branco_info['hora'].replace(hour=nova_hora % 24, minute=novo_minuto, second=0)
    return proximo_horario

# Exemplo de uso
branco_info = {'hora': datetime.strptime("01:58", "%H:%M")}
anterior = 1
posterior = 7
proximo = estrategia_2(branco_info, anterior, posterior)
print("Previsão:", proximo.strftime("%H:%M"))
