import itertools
import numpy as np


def recolnamer (con=None, set_exclude=set(['TARGET']), enable_aka=False):
    set_exclude = set(set_exclude)
    cursor = con.cursor()  

    cursor.execute("""SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';""")  #AND TABLE_CATALOG='risk' 
    table_names = np.array(cursor.fetchall())[:, 0]

    header = {}
    column_names = {}
    column_renamed = {}

    for table_name in table_names:
        cursor.execute(f"""select column_name from information_schema.columns where table_name = '{table_name}';""")
        column_names[table_name] = set(np.array(cursor.fetchall())[:, 0]) - set_exclude
        column_renamed[table_name] = []

        if enable_aka:
            header[table_name] = str().join([term[0] for term in table_name.split('_')])
        else:
            header[table_name] = table_name
        

        print(column_names[table_name])

    duplicated = None

    for table_A, table_B in itertools.combinations(table_names, 2):
        duplicated = None
        print(table_A, table_B)
        duplicated = column_names[table_A] & column_names[table_B]

        print(duplicated)

        for column_name in duplicated:
            if not column_name in column_renamed[table_A]:
                print(f"""SP_RENAME '[dbo].[{table_A}].[{column_name}]', '{header[table_A]}_{column_name}', 'COLUMN';""")
                cursor.execute(f"""SP_RENAME '[dbo].[{table_A}].[{column_name}]', '{header[table_A]}_{column_name}', 'COLUMN';""")
                column_renamed[table_A].append(column_name)

            if not column_name in column_renamed[table_B]:
                print(f"""SP_RENAME '[dbo].[{table_B}].[{column_name}]', '{header[table_B]}_{column_name}', 'COLUMN';""")
                cursor.execute(f"""SP_RENAME '[dbo].[{table_B}].[{column_name}]', '{header[table_B]}_{column_name}', 'COLUMN';""")
                column_renamed[table_B].append(column_name)

    con.commit()
    con.close()

"""

if __name__ == '__main__':
    import pymssql  


    con = pymssql.connect(server='***', database='***')

    recolnamer(con, enable_aka=True)

"""