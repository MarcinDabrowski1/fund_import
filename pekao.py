import psycopg2
import pandas as pd


conn = psycopg2.connect(
    host="prism.c6rv89t9u1ls.eu-central-1.rds.amazonaws.com",
    database="prism",
    user="postgres",
    password="postgres")

restart_count = 0
cursor = conn.cursor()
pekao_data = pd.read_csv('funds.csv')
row_data = pekao_data.values.tolist()


for a in range(1, len(pekao_data["0"][1:])+1):
    date = pekao_data["0"][a]
    for i in range(1, len(row_data[1][1:])+1):
        price = row_data[a][i]
        # currency = row_data[0][i].split("(")[1][:-1]
        name = row_data[0][i]
        # clas = row_data[0][i].split(" (")[0][-1]
        if price != "bd":
            cursor.execute("INSERT INTO tfipekao (date, price, name) VALUES(%s, %s, %s)", (date, price, name))
            conn.commit()


conn.close()
