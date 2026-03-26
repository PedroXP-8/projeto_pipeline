import sqlite3 
import pandas as pd



# 1: count of all insurance providers
def query_insurance_providers():

    conn = sqlite3.connect('Database/hospital.db')
    query1 = """ 
    select insurance_provider, count(*) as count
    from patients group by insurance_provider
    order by count desc;
    """
    df_1 = pd.read_sql_query(query1, conn)

    print("Count of all insurance providers:")
    print(df_1)

    conn.commit()
    conn.close()

# 2: patients over than 50 years old
def query_patients_over_50():

    conn = sqlite3.connect('Database/hospital.db')
    query2 = """
    select name, age, gender, email from patients
    where age >= 50
    order by age desc;
    """

    df_2 = pd.read_sql_query(query2, conn)
    print("\nPatients over 50 years old:")
    print(df_2)

    conn.commit()
    conn.close()


# 3: general informations about patients
def query_general_information():

    conn = sqlite3.connect('Database/hospital.db')
    query3 = """
    select p.name as "patient name", p.age,
    a.reason_for_visit, a.appointment_date,
    d.name as "doctor name", t.cost as "treatment cost" 
    from patients p
    join appointments a 
        on p.IDpatient = a.IDpatient
    join doctors d
        on a.IDdoctor = d.IDdoctor
    join treatments t
        on a.IDappointment = t.appointment_id
    order by appointment_date desc
    limit 20;
    """

    df_3 = pd.read_sql_query(query3, conn)
    print("\nGeneral information about patients:")
    print(df_3)

    conn.commit()
    conn.close()


# 4: count of appointments per doctor
def query_appointments_per_doctor():

    conn = sqlite3.connect('Database/hospital.db')
    query4 = """
    select d.name as "doctor name", d.specialization,
    d.hospital_branch, count(*) as "number of appointments"
    from doctors d
    join appointments a
        on d.IDdoctor = a.IDdoctor
    group by d.name, d.specialization, d.hospital_branch
    order by "number of appointments" desc
    limit 20;
    """ 

    df_4 = pd.read_sql_query(query4, conn)
    print("\nCount of appointments per doctor:")
    print(df_4)

    conn.commit()
    conn.close()


