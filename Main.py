import tables
import transform
import extract
import load

def main():

    # Extracting data
    extract_doctors = extract.extract_data("../data/raw/doctors.csv")
    extract_patients = extract.extract_data("../data/raw/patients.csv")
    extract_appointments = extract.extract_data("../data/raw/appointments.csv")
    extract_treatments = extract.extract_data("../data/raw/treatments.csv")
    extract_billings = extract.extract_data("../data/raw/billings.csv")

    # Transforming data
    transform_doctors = transform.transform_doctors(extract_doctors)
    transform_patients = transform.transform_patients(extract_patients)
    transform_appointments = transform.transform_appointments(extract_appointments)
    transform_treatments = transform.transform_treatments(extract_treatments)
    transform_billings = transform.transform_billings(extract_billings)

    # creating tables
    tables.create_doctors_table()
    tables.create_patients_table()
    tables.create_appointments_table()
    tables.create_treatments_table()
    tables.create_billings_table()

    # loading data
    load.load_data(transform_doctors, transform_patients, transform_appointments, transform_treatments, transform_billings)

if __name__ == "__main__":
    main()


