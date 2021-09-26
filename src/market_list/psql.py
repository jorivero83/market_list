import psycopg2


class Query:

    def __init__(self, **params):
        self.credentials = params
        self.connection = self.create_connection()

    def __del__(self):
        if self.connection is not None:
            self.connection.close()

    def create_connection(self):
        conn = None
        try:
            conn = psycopg2.connect(**self.credentials)
        except Exception as e:
            raise IOError(e)

        return conn

    def run(self, txt: str):
        """
        This function execute the input query (`txt`) into database using psycopg2
        and return the results as dictionary.

        :param txt: Query to be executed in database.
        :return: A dictionary with `description` and `data`.
                 If DataFrame, `description` are the headers of columns.

        Examples:

            credentials = {'database': "lista_compra", 'user': "postgres",
                           'password': 'pass', 'host': "localhost",
                           'port': "5432"}

            # Get the maximum id of a table as a number
            query_str = "SELECT max(id) from ingredientes"
            res = Query(**credentials).run(txt=query_str)
            print(res['data'][0][0])

            # Get values from table as DataFrame
            query_str = "select t1.name, t1.units, sum(t1.size) as size
                         from ingredientes as t1
                         inner join recetas as t2
                         on t1.receta_id = t2.id
                         where t2.id in (1, 5, 6)
                            and t1.name not in ('agua')
                         GROUP by t1.name, t1.units
                         order by size desc"
            res = Query(**credentials).run(txt=query_str)
            print(pd.DataFrame(res['data'], columns=res['description']))
        """
        description = None
        records = None
        try:
            # Query to PostgreSQL database
            cursor = self.connection.cursor()
            cursor.execute(txt)
            description = [desc[0] for desc in cursor.description]
            records = cursor.fetchall()
            cursor.close()
        except Exception as e:
            raise IOError(e)

        return {'description': description, 'data': records}


if __name__ == '__main__':
    import pandas as pd
    from tabulate import tabulate

    pd.set_option('display.width', 320)
    pd.set_option('display.max_columns', 30)
    credentials = {
        'database': "lista_compra",
        'user': "postgres",
        'password': 'pass',
        'host': "localhost",
        'port': "5432"
    }

    # RECETAS CON INGREDIENTES
    query_str = """select t2.id, t2.name, count(t1.id) as num_ingredientes 
                from ingredientes as t1
                inner join recetas as t2
                on t1.receta_id = t2.id
                GROUP by t2.id, t2.name
                order by t2.id"""
    res = Query(**credentials).run(txt=query_str)
    df = pd.DataFrame(res['data'], columns=res['description'])
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # query_str = "SELECT id from recetas"
    # res = Query(**credentials).run(txt=query_str)
    # v_list = [a[0] for a in res['data']]
    # print([b for b in [2, 34] if b not in v_list])

    # query_str = "SELECT max(id) from recetas"
    # res = Query(**credentials).run(txt=query_str)
    # print(res['data'][0][0])

    # Get values from table as DataFrame
    # query_str = """select t1.name as ingredientes, t1.units, sum(t1.size) as size
    #                from ingredientes as t1
    #                inner join recetas as t2
    #                on t1.receta_id = t2.id
    #                where t2.id in (1, 5, 6)
    #                      and t1.name not in ('agua')
    #                group by t1.name, t1.units
    #                order by size desc"""
    # res = Query(**credentials).run(txt=query_str)
    # df = pd.DataFrame(res['data'], columns=res['description'])
    # print(tabulate(df, headers='keys', tablefmt='psql'))

    # query_str = """select id, name as receta from recetas order by id"""
    # res = Query(**credentials).run(txt=query_str)
    # df = pd.DataFrame(res['data'], columns=res['description'])
    # print(tabulate(df, headers='keys', tablefmt='markdown', showindex="never"))
