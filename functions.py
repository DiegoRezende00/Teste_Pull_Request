import time
def tempo_execucao():
    inicio = time.time()
    time.sleep(5)
    fim = time.time()
    tempo_execucao_codigo = fim - inicio
    return tempo_execucao_codigo