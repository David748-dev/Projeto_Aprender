import pandas as pd
import os

nome_arquivo = "Travas Backflush.xlsx"
aba_arquivo = "Travas Backflush"
caminho_arquivo_origem = r"\\brspesp-fp03\groupe01$\Group\MATERIAIS\Grupo - Análise de Inventário\49 - Base de Dados\01 - Fato\Travas Backflush.xlsx"
caminho_arquivo_destino = r"\\brspesp-fp03\groupe01$\Group\MATERIAIS\Grupo - Análise de Inventário\49 - Base de Dados\01 - Fato\00 - Backflush\Travas Backflush.parquet"

df = pd.read_excel(caminho_arquivo_origem, sheet_name=aba_arquivo)

# Converter a coluna "Item" para string
df['Item'] = df['Item'].astype(str)

df.to_parquet(caminho_arquivo_destino, engine='pyarrow', index=False)
print(f"✅ Arquivo salvo em: {caminho_arquivo_destino}")



