import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))




class Patient:
    def __init__(self,patient_id, name, age, gender, contact_info, diagnosis=None, treatment_plan=None):
        self.patient_id = patient_id
        self.name= name
        self.age= age
        self.gender= gender
        self.contact_info= contact_info
        self.diagnosis= diagnosis
        self.treatment_plan = treatment_plan
        self.assigned_doctor = None
        self.appointments = []     #List of appoinments (Object)
        self.medical_record = MedicalRecord(self)
                                            

    # The __str__ methods represents how the Object should be represented as a string so we could use print(Object) right away.    
    def __str__(self):
        return f"The patient's name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nContact: {self.contact_info}"
    

    def assign_doctor(self, doctor):
        self.assigned_doctor = doctor
        print(f"Doctor {doctor.name} assigned to patient {self.name}.\n")

    def add_appointment(self, appointment):
        self.appointments.append(appointment) 



################################################################################                                                    


class Doctor:
    def __init__(self,doctor_id,name,specialization,experience,contact_info):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.experience = experience
        self.contact_info = contact_info
        self.list_of_patients = []
        self.doctor_dict = {}
        

    def __str__(self):
        return f"Docotrs\'s name: {self.name}\nSpecialization: {self.specialization}\nExperience:{self.experience}\nContact: {self.contact_info}"

    
    def assign_patient(self, patient):
        self.list_of_patients.append(patient)
        print(f"Patient {patient.name} assigned to doctor {self.name}.\n")

################################################################################                                                    



class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, Date: {self.date}, Time: {self.time}"

################################################################################   





class MedicalRecord:
    def __init__(self, patient):
        self.patient = patient
        self.diagnoses = []
        self.medications = []    #list of dictionaries
        self.visit_records = []  

    def add_diagnosis(self, diagnosis):
        self.diagnoses.append(diagnosis)
        print(f"Diagnosis added for {self.patient.name}: {diagnosis}\n")

    def add_medication(self, medication, dosage, frequency):
        self.medications.append({"medication": medication, "dosage": dosage, "frequency": frequency})
        print(f"Medication added for {self.patient.name}: {medication}, Dosage: {dosage}, Frequency: {frequency}\n")

    def add_visit_record(self, visit_record):
        self.visit_records.append(visit_record)
        print(f"Visit record added for {self.patient.name}: {visit_record}\n")

    def view_records(self):
        print(f"Medical Records for {self.patient.name}:")
        print(f"Diagnoses: {self.diagnoses}")
        print(f"Medications: {self.medications}")
        print(f"Visit Records: {self.visit_records}")



                                    




