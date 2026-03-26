import sys
sys.path.append('Pipeline')
sys.path.append('Sql')

from Pipeline import tables
from Pipeline import transform
from Pipeline import load
from Pipeline import extract
from Sql import queries


def main():

    # Extracting data
    extract_doctors = extract.extract_data("Data/Raw/doctors.csv")
    extract_patients = extract.extract_data("Data/Raw/patients.csv")
    extract_appointments = extract.extract_data("Data/Raw/appointments.csv")
    extract_treatments = extract.extract_data("Data/Raw/treatments.csv")
    extract_billings = extract.extract_data("Data/Raw/billing.csv")

    # Transforming data
    df_doctors = transform.transform_doctors(extract_doctors)
    df_patients = transform.transform_patients(extract_patients)
    df_appointments = transform.transform_appointments(extract_appointments)
    df_treatments = transform.transform_treatments(extract_treatments)
    df_billings = transform.transform_billing(extract_billings)

    # creating tables
    tables.create_doctors_table()
    tables.create_patients_table()
    tables.create_appointments_table()
    tables.create_treatments_table()
    tables.create_billings_table()

    # loading data
    load.load_data(df_doctors, df_patients, df_appointments, df_treatments, df_billings)

    # running queries
    queries.query_insurance_providers()
    queries.query_patients_over_50()
    queries.query_general_information()
    queries.query_appointments_per_doctor()
    
    print("All queries executed successfully.")

if __name__ == "__main__":
    main()


