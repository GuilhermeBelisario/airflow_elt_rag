from langchain_openai import ChatOpenAI ,OpenAIEmbeddings   
import duckdb
import pandas as pd

class Ragnarok :

    def __init__(self, pg_config: dict, tamanho_maximo: int, prompt: str, query: str):
        self.pg_config = pg_config
        self.tamanho_maximo = tamanho_maximo
        self.prompt = prompt
        self.query = query
        self.llm = ChatOpenAI(model='gpt-4.1-mini', temperature=0)
        self.embeddings = OpenAIEmbeddings(
            model='text-embedding-3-large-v2'
            )

    def extrair_dados(duckdb_conn: duckdb.DuckDBPyConnection, query: str):
        
        lista_texto = []

        df = duckdb_conn.execute(query).fetchdf()
        for item in df.column(1):
            lista_texto.append(item)

        return lista_texto

    def quebrar_chuncks(self, lista_texto: list, tamanho_maximo: int):


        return texto_quebrado
    
    def categorizar(self, texto_quebrado: str, prompt: str):
        

        pass

    def transformar_dados(self, dados): 
        # Lógica para transformar os dados extraídos
        pass
    def carregar_dados(self, dados_transformados):  
        # Lógica para carregar os dados transformados para o destino
        pass    # Lógica para a tarefa ETL
    
    