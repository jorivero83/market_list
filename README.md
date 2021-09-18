# market_list

This is project to generate the market list based on a kitchen recipes list.

Example:

We have already in our database the following recipes list:

1. Pollo chimichurri
2. Lentejas guisadas con verduras
3. Ternera stroganoff
4. Verduras y pavo al vapor
5. Arroz con atún
6. Salmón y arroz bastami
7. Crema espinaca con nuez
8. Pisto
9. Pesto
10. Tinga de pollo
11. Salsa boloñesa
12. Arroz cremoso de pollo y verduras

Choosing recipes (1, 5, 6), if we want to go to the market now, we need the list of ingredients and how much of each one
need to buy. Then, for this purpose you use our package as bellow, and you can know the ingredients and the quantities
to buy.

Python code

```python
from market_list.engine import MarketList
from tabulate import tabulate

credentials = {
    'database': "lista_compra",
    'user': "postgres",
    'password': 'pass',
    'host': "localhost",
    'port': "5432"
}
df = MarketList(**credentials).create(recipes=[1, 5, 6])
print(tabulate(df, headers='keys', tablefmt='psql', showindex="never"))
```

Results:

```
+----+----------------------------------+----------+--------+
|    | ingredients                      | units    |   size |
|----+----------------------------------+----------+--------|
|  0 | muslos de pollo                  | gramos   |    800 |
|  1 | arroz largo                      | gramos   |    350 |
|  2 | pimiento rojo                    | gramos   |    120 |
|  3 | pimiento verde                   | gramos   |    120 |
|  4 | vino blanco                      | gramos   |    100 |
|  5 | aceite de oliva                  | gramos   |     50 |
|  6 | maizena                          | gramos   |     20 |
|  7 | dientes de ajo                   | unidades |      6 |
|  8 | latas de atún en aceite de oliva | unidades |      3 |
|  9 | ramas de perejil                 | unidades |      2 |
| 10 | pastilla de caldo de pescado     | unidades |      1 |
| 11 | cucharadita de sal               | unidades |      1 |
| 12 | cucharadita de orégano           | unidades |      1 |
| 13 | cucharadita de pimentón          | unidades |      1 |
+----+----------------------------------+----------+--------+
```
