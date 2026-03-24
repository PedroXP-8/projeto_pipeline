from extract import extract_data
import pandas as pd

def transform_doctors(df):

    # data type treatment
    df["specialization"] = df["specialization"].apply(lambda x: str(x))
    df["phone_number"] = df["phone_number"].apply(lambda x: str(x))
    df["hospital_branch"] = df["hospital_branch"].apply(lambda x: str(x))
    df["email"] = df["email"].apply(lambda x: str(x))
    
    #columns treatment
    df = df.rename(columns={"doctor_id": "IDdoctor"})
    df["IDdoctor"] = range(1, len(df) + 1) 

    df["name"] = df["first_name"] + " " + df["last_name"]
    df = df.drop(columns=["first_name", "last_name"])

    cols = list(df.columns)
    df = df[[cols[0]] + [cols[-1]] + cols[1:-1]]

    df.to_csv("../data/processed/treated_doctors.csv", index=False)

    return df
    

def transform_patients(df):

    # data type treatment
    df["gender"] = df["gender"].apply(lambda x: str(x))
    df["contact_number"] = df["contact_number"].apply(lambda x: str(x))
    df["address"] = df["address"].apply(lambda x: str(x))
    df["insurance_provider"] = df["insurance_provider"].apply(lambda x: str(x))
    df["insurance_number"] = df["insurance_number"].apply(lambda x: str(x))
    df["email"] = df["email"].apply(lambda x: str(x))

    df["date_of_birth"] = pd.to_datetime(df["date_of_birth"], format="%Y-%m-%d").dt.date
    df["registration_date"] = pd.to_datetime(df["registration_date"], format="%Y-%m-%d").dt.date

    #columns treatment
    df = df.rename(columns={"patient_id": "IDpatient"})
    df["IDpatient"] = range(1, len(df) + 1) 

    df["name"] = df["first_name"] + " " + df["last_name"]
    df = df.drop(columns=["first_name", "last_name"])

    cols = list(df.columns)
    cols.remove("name")
    cols.insert(1, "name")

    df = df[cols]

    df.to_csv("../data/processed/treated_patients.csv", index=False)

    return df


def transform_treatments(df):

    # data type treatment
    df["treatment_type"] = df["treatment_type"].apply(lambda x: str(x))
    df["description"] = df["description"].apply(lambda x: str(x))
    
    df["treatment_date"] = pd.to_datetime(df["treatment_date"], format="%Y-%m-%d")

     #columns treatment
    df = df.rename(columns={"treatment_id": "IDtreatment"})
    df["IDtreatment"] = range(1, len(df) + 1) 
    df["appointment_id"] = range(1, len(df) + 1) 

    df.to_csv("../data/processed/treated_treatments.csv", index=False)

    return df


def transform_appointments(df):

    # data type treatment
    df["reason_for_visit"] = df["reason_for_visit"].apply(lambda x: str(x))
    df["status"] = df["status"].apply(lambda x: str(x))
    
    df["appointment_date"] = pd.to_datetime(df["appointment_date"], format="%Y-%m-%d")
    df["appointment_time"] = pd.to_datetime(df["appointment_time"], format="%H:%M:%S").dt.time

    #columns treatment

    df = df.rename(columns={"appointment_id": "IDappointment"})
    df["IDappointment"] = range(1, len(df) + 1)

    df["patient_id"] = df["patient_id"].str[1:]
    df["patient_id"] = pd.to_numeric(df["patient_id"], errors="coerce").astype(int)
    df = df.rename(columns={"patient_id": "IDpatient"})
    
    df["doctor_id"] = df["doctor_id"].str[1:]
    df["doctor_id"] = pd.to_numeric(df["doctor_id"], errors="coerce").astype(int)
    df = df.rename(columns={"doctor_id": "IDdoctor"})

    df.to_csv("../data/processed/treated_appointments.csv", index=False)

    return df


def transform_billing(df):

    # data type treatment
    df["payment_status"] = df["payment_status"].apply(lambda x: str(x))
    df["payment_method"] = df["payment_method"].apply(lambda x: str(x))
    
    df["bill_date"] = pd.to_datetime(df["bill_date"], format="%Y-%m-%d")

    #columns treatment

    df = df.rename(columns={"bill_id": "IDbill"})
    df["IDbill"] = range(1, len(df) + 1)

    df["patient_id"] = df["patient_id"].str[1:]
    df["patient_id"] = pd.to_numeric(df["patient_id"], errors="coerce").astype(int)
    df = df.rename(columns={"patient_id": "IDpatient"})
    df["treatment_id"] = df["treatment_id"].str[1:]
    df["treatment_id"] = pd.to_numeric(df["treatment_id"], errors="coerce").astype(int)
    df = df.rename(columns={"treatment_id": "IDtreatment"})

    df.to_csv("../data/processed/treated_billings.csv", index=False)

    return df
