import time
def tempo_execucao():
    inicio = time.time()
    time.sleep(3)
    fim = time.time()
    tempo_execucao_codigo = fim - inicio
    return tempo_execucao_codigo