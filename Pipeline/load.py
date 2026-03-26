import sqlite3



def load_data(df1, df2, df3, df4, df5):

    conn = sqlite3.connect("Database/hospital.db")
    df1.to_sql("doctors", conn, if_exists="replace", index=False)
    df2.to_sql("patients", conn, if_exists="replace", index=False)
    df3.to_sql("appointments", conn, if_exists="replace", index=False)
    df4.to_sql("treatments", conn, if_exists="replace", index=False)
    df5.to_sql("billings", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

