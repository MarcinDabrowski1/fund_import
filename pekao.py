import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="prism.c6rv89t9u1ls.eu-central-1.rds.amazonaws.com",
    database="prism",
    user="postgres",
    password="postgres")


pekao_data = pd.read_csv('funds.csv')
cursor = conn.cursor()

row_data = pekao_data.values.tolist()


for a in range(1, len(pekao_data["0"][1:])+1):
    v1 = pekao_data["0"][a]
    for i in range(1, len(row_data[1][1:])+1):
        v2 = row_data[a][i]
        v3 = row_data[0][i].split("(")[1][:-1]
        v4 = row_data[0][i]
        v5 = row_data[0][i].split(" (")[0][-1]
        if v2 != "bd":
            cursor.execute("INSERT INTO tfipekao (date, price, currency, name, class) VALUES(%s, %s, %s, %s, %s)", (v1, v2, v3, v4, v5))
            conn.commit()


conn.close()
