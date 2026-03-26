import sqlite3

def create_doctors_table():
    conn = sqlite3.connect("Database/hospital.db")
    cursor = conn.cursor()

    cursor.execute(""" create table if not exists doctors (
                        IDdoctor integer primary key,
                        name varchar(30) not null,
                        specialization varchar(20) not null,
                        phone_number varchar(15) not null,
                        years_experience integer not null,
                        hospital_branch varchar(20) not null,
                        email varchar(40) not null unique,
                        salary numeric(10,2),
                        increase float);
                        """)
    conn.commit()
    conn.close()

def create_patients_table():
    conn = sqlite3.connect("Database/hospital.db")
    cursor = conn.cursor()

    cursor.execute(""" create table if not exists patients (
                        IDpatient integer primary key,
                        name varchar(30) not null,
                        gender char(1) not null,
                        date_of_birth date not null,
                        contact_number varchar(15) not null,
                        address varchar(20) not null,
                        registration_date date not null,
                        insurance_provider varchar(20) not null,
                        insurance_number char(9) not null,
                        email varchar(40) not null unique,
                        age integer not null);
                        """)
    conn.commit()
    conn.close()

def create_appointments_table():
    conn = sqlite3.connect("Database/hospital.db")
    cursor = conn.cursor()

    cursor.execute(""" create table if not exists appointments (
                        IDappointment integer primary key,
                        ID_patient integer,
                        ID_doctor integer,
                        appointment_date date not null,
                        appointment_time time not null,
                        reason_for_visit varchar(100) not null,
                        status varchar(10) not null,
                        constraint fk_appointment_ID_patient
                        foreign key (ID_patient) references patients(IDpatient),
                        constraint fk_appointment_ID_doctor
                        foreign key (ID_doctor) references doctors(IDdoctor));
                        """)
    conn.commit()
    conn.close()

def create_treatments_table():
    conn = sqlite3.connect("Database/hospital.db")
    cursor = conn.cursor()

    cursor.execute(""" create table if not exists treatments (
                        IDtreatment integer primary key,
                        ID_appointment integer,
                        treatment_type varchar(20) not null,
                        description varchar(40) not null,
                        cost numeric(10,2) not null,
                        treatment_date date not null,
                        constraint fk_treatment_ID_appointment
                        foreign key (ID_appointment) references appointments(IDappointment));
                        """)
    conn.commit()
    conn.close()


def create_billings_table():
    conn = sqlite3.connect("Database/hospital.db")
    cursor = conn.cursor()

    cursor.execute(""" create table if not exists billings (
                        IDbilling integer primary key,
                        ID_patient integer,
                        ID_treatment integer,
                        bill_date date not null,
                        payment_method varchar(10) not null,
                        payment_status varchar(15) not null,
                        constraint fk_billing_ID_patient
                        foreign key (ID_patient) references patients(IDpatient),
                        constraint fk_billing_ID_treatment
                        foreign key (ID_treatment) references treatments(IDtreatment));
                        """)
    conn.commit()
    conn.close()
