import psycopg2

class DatabaseConnector:
    
    def __init__(self, pg_config):

        self.pg_config = pg_config
    