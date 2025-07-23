import pandas as pd
import time
import functions

tempo_execucao_codigo = functions.tempo_execucao()

print(f"O código levou {tempo_execucao_codigo:.2f} segundos para rodar")