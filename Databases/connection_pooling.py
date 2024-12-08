# Connection Pooling

from psycopg2 import pool

class DatabaseConnectionPool:

    def __init__(self, dbname: str, user: str, password: str, host: str, port: str, min_conn=1, max_conn=10):

        self.db_config = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }

        self.connection_pool = None
        self.create_pool(min_conn, max_conn)

    def create_pool(self, min_conn: int, max_conn: int):
        try:
            self.connection_pool = pool.SimpleConnectionPool(
                min_conn,
                max_conn,
                **self.db_config
            )
            if self.connection_pool:
                print("Connection pool created successfully.")
        except Exception as e:
            print(f"Error creating connection pool: {e}")

    def get_connection(self):
        return self.connection_pool.getconn()

    def put_connection(self, conn):
        self.connection_pool.putconn(conn)

    def close_all_connections(self):
        if self.connection_pool:
            self.connection_pool.closeall()
            print("All connections in the pool have been closed.")

class DatabaseOperations:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool

    def execute_query(self, query):
        conn = self.connection_pool.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                return results
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            self.connection_pool.put_connection(conn)

if __name__ == "__main__":

    dbname = 'your_database'
    user = 'your_user'
    password = 'your_password'
    host = 'localhost'
    port = '5432'

    # Create a connection pool
    db_pool = DatabaseConnectionPool(dbname, user, password, host, port)

    # Create an instance of DatabaseOperations
    db_operations = DatabaseOperations(db_pool)

    # Example query
    query = "SELECT * FROM your_table;"
    results = db_operations.execute_query(query)
    
    if results:
        for row in results:
            print(row)

    # Close all connections in the pool at the end
    db_pool.close_all_connections()