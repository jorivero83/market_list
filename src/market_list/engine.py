import pandas as pd
from market_list.psql import Query
import warnings


class MarketList:

    def __init__(self, **params):
        self.credentials = params

    def check_recipes(self, recipes):
        txt = "SELECT id from recetas"
        results = Query(**self.credentials).run(txt=txt)
        v_list = [a[0] for a in results['data']]
        checked_list = [a for a in recipes if a not in v_list]
        if len(checked_list)>0:
            msg = 'There are some recipes unkowns. Please check recipes: {}!'.format(checked_list)
            warnings.warn(msg)

    def create(self, recipes):
        self.check_recipes(recipes)
        recipes_str = ",".join([str(a) for a in recipes])
        txt = """
        select t1.name as ingredients, t1.units, sum(t1.size) as size
        from ingredientes as t1
        inner join recetas as t2
        on t1.receta_id = t2.id
        where t2.id in ({0})
        and t1.name not in ('agua')
        group by t1.name, t1.units
        order by size desc""".format(recipes_str)
        results = Query(**self.credentials).run(txt=txt)
        if results['data']:
            return pd.DataFrame(results['data'], columns=results['description'])
        else:
            raise IOError("Unkown input recipes!")


if __name__ == '__main__':
    from tabulate import tabulate

    credentials = {
        'database': "lista_compra",
        'user': "postgres",
        'password': 'pass',
        'host': "localhost",
        'port': "5432"
    }
    df = MarketList(**credentials).create(recipes=[1, 16, 17, 11, 12])
    df.to_csv("/home/jrd/Documents/market_list/output/list_week.csv", index=False)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex="never"))

