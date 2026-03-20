from extract import extract_data
import pandas as pd

def transform_doctors(df):

    # data type treatment
    df = df.astype({
        "first_name": str,
        "last_name": str,
        "specialization": str,
        "phone_number": str,
        "hospital_branch": str,
        "email": str
    })

    #columns treatment
    df["doctor_id"] = df["IDdoctor"]
    df["IDdoctor"] = range(1, len(df) + 1) 

    df["name"] = df["first_name"] + " " + df["last_name"]
    df.drop(["first_name", "last_name"], axis=1)

    return df

def transform_patients(df):

    # data type treatment
    df = df.astype({
        "first_name": str,
        "last_name": str,
        "gender": str,
        "contact_number": str,
        "address": str,
        "insurancer_provider": str,
        "insurance_number": str,
        "email": str
    })

    df = pd.to_datetime(df["date_of_birth"], format="%Y/%m/%d").dt.date
    df = pd.to_datetime(df["registration_date"], format="%Y/%m/%d").dt.date

    #columns treatment
    df["patient_id"] = df["IDpatient"]
    df["IDpatient"] = range(1, len(df) + 1) 

    df["name"] = df["first_name"] + " " + df["last_name"]
    df.drop(["first_name", "last_name"], axis=1)

    return df

def transform_treatments(df):

    # data type treatment
    df = df.astype({
        "treatment_type": str,
        "description": str
    })
    df = pd.to_datetime(df["treatment_date"], format="%Y/%m/%d").dt.date

     #columns treatment
    df["treatment_id"] = df["IDtreatment"]
    df["IDtreatment"] = range(1, len(df) + 1) 

    df["appointment_id"] = range(1, len(df) + 1) 

    df["name"] = df["first_name"] + " " + df["last_name"]
    df.drop(["first_name", "last_name"], axis=1)

    return df

def transform_appointment(df):

    # data type treatment
    df = df.astype({
        "reason_for_visit": str,
        "status": str
    })
    df = pd.to_datetime(df["appointment_date"], format="%Y/%m/%d").dt.date
    df = pd.to_datetime(df["appointment_date"], format="%H:%M").dt.time

    #columns treatment

    df["appointment_id"] = df["IDappointment"]
    df["IDappointment"] = range(1, len(df) + 1)

    df["patient_id"] = df["patient_id"].str[1:]
    df["patient_id"] = pd.to_numeric(df["patient_id"], erros="coerce").astype(int)
    df["doctor_id"] = df["doctor_id"].str[1:]
    df["doctor_id"] = pd.to_numeric(df["doctor_id"], erros="coerce").astype(int)

    return df

def transform_billing(df):

    # data type treatment
    df = df.astype({
        "payment_status": str,
        "payment_method": str
    })
    
    df = pd.to_datetime(df["bill_date"], format="%Y/%m/%d").dt.date

    #columns treatment

    df["bill_id"] = df["IDbill"]
    df["IDbill"] = range(1, len(df) + 1)

    df["patient_id"] = df["patient_id"].str[1:]
    df["patient_id"] = pd.to_numeric(df["patient_id"], erros="coerce").astype(int)
    df["treatment_id"] = df["treatment_id"].str[1:]
    df["treatment_id"] = pd.to_numeric(df["treatment_id"], erros="coerce").astype(int)

    return df
