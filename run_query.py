from market_list.engine import MarketList
from tabulate import tabulate

if __name__ == '__main__':
    credentials = {
        'database': "lista_compra",
        'user': "postgres",
        'password': 'pass',
        'host': "localhost",
        'port': "5432"
    }
    df = MarketList(**credentials).create(recipes=[1, 2, 4, 10, 12])
    # df.to_csv("/home/jrd/Documents/market_list/output/list_week_.csv", index=False)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex="never"))

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages

    fig, ax = plt.subplots(figsize=(8.27, 11.69), dpi=100)  # for landscape figsize=(11.69, 8.27)
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df.values, colLabels=df.columns,
                         loc='center', colLoc='right', colWidths=(0.25, 0.15, 0.15))
    the_table.set_fontsize(14)
    the_table.scale(1.5, 1.5)  # may help
    # plt.show()
    pp = PdfPages('/home/jrd/Documents/market_list/output/multipage.pdf')
    pp.savefig()
    pp.close()

    # History of recipes
    # 1- week: 2021-09-20 - 2021-09-24, recipes: [1, 16, 17, 11, 12]
    # 2- week: 2021-09-27 - 2021-10-01, recipes: [1, 2, 4, 10, 12]
