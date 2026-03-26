import sqlite3

conn = sqlite3.connect("hospital.db")

def load_data(df1, df2, df3, df4, df5):
    df1.to_sql("doctors", conn, if_exists="append", index=False)
    df2.to_sql("patients", conn, if_exists="append", index=False)
    df3.to_sql("appointments", conn, if_exists="append", index=False)
    df4.to_sql("treatments", conn, if_exists="append", index=False)
    df5.to_sql("billings", conn, if_exists="append", index=False)

