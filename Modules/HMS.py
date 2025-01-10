from my_classes import Doctor, Patient, MedicalRecord, Appointment


from os import system, name

# import sleep to show output for some time period
from time import sleep




def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')




class HospitalManagmentSystem:
    def __init__(self):
        self.patients_dict = {}
        self.doctor_dict = {}
        self.appointments = {}

################################################################################                                                    

    def add_patient(self, patient_id, name, age, gender, contact_info, diagnosis=None, treatment_plan=None):
        if patient_id in self.patients_dict:
            print(f"Patient with ID {patient_id} already exists.\n")
        else:
            patient = Patient(patient_id, name, age, gender, contact_info, diagnosis, treatment_plan)
            self.patients_dict[patient_id] = patient

            #globals()[f"patient_{patient_id}"] = MedicalRecord(self.patients_dict[patient_id])
  
            print(f"Patient {name} added successfully.\n") 



    def add_doctor(self,doctor_id,name,specialization,experience,contact_info):
        if doctor_id in self.doctor_dict:
            print(f"The doctor with ID {self.doctor_id} is already on the system")
        else:    
            doctor= Doctor(doctor_id,name,specialization,experience,contact_info)
            self.doctor_dict[doctor_id]= doctor        
            print(f"Doctor {doctor.name} added successfully\n")
         
################################################################################     

    def display_patient_info(self, patient_id):
        if patient_id in self.patients_dict:
            patient = self.patients_dict[patient_id]
            print(f"{patient}\n")


    def display_doctor_info(self, doctor_id):
        if doctor_id in self.doctor_dict:
            doctor = self.doctor_dict[doctor_id]
            print(f"{doctor}\n")            


################################################################################                                                    



    def update_patient(self,patient_id, name= None, age = None, gender= None, contact_info= None, diagnosis=None, treatment_plan=None):
        if name:
            self.patients_dict[patient_id].name = name
        if age:
           self.patients_dict[patient_id].age = age
        if gender:
            self.patients_dict[patient_id].gender = gender
        if contact_info:
            self.patients_dict[patient_id].contact_info = contact_info    
        if diagnosis:
            self.patients_dict[patient_id].diagnosis = diagnosis     
        if treatment_plan:
            self.patients_dict[patient_id].treatment_plan = treatment_plan    


################################################################################                                                    
    def delete_patient(self,patient_id):
        if patient_id in self.patients_dict:
            self.patients_dict.pop(patient_id)
            print(f"Patient with ID {patient_id} deleted successfully.\n")    

        else:
            print(f"Patient with ID {patient_id} does not exist.")    



################################################################################                                                    

    # search_term could be an ID or a name
    def search_patient(self, search_term):
        found = False
        #.values returns a list of all the values in the dictionary 
        for patient in self.patients_dict.values():         
            if search_term in (patient.name, patient.patient_id):
                print(f"{patient}\n")
                found = True
        if not found:
            print(f"No patient found with term: {search_term}\n")



    def search_doctor(self, search_term):
        found = False
        #.values returns a list of all the values in the dictionary 
        for doctor in self.doctor_dict.values():         
            if search_term in (doctor.name, doctor.specialization):
                print(f"{doctor}\n")
                found = True
        if not found:
            print(f"No Doctor found with term: {search_term}\n")


################################################################################     

    def assign_doctor_to_patient(self, doctor_id, patient_id):
        if doctor_id in self.doctor_dict and patient_id in self.patients_dict:
            doctor = self.doctor_dict[doctor_id]
            patient = self.patients_dict[patient_id]
            doctor.assign_patient(patient)
            patient.assign_doctor(doctor)
        else:
            print(f"Doctor or Patient not found.")


################################################################################     

    def book_appointment(self, appointment_id, patient_id, doctor_id, date, time):
        if patient_id in self.patients_dict and doctor_id in self.doctor_dict:
            patient = self.patients_dict[patient_id]
            doctor = self.doctor_dict[doctor_id]
            appointment = Appointment(appointment_id, patient, doctor, date, time)
            patient.add_appointment(appointment)
            doctor.assign_patient(patient)
            self.appointments[appointment_id] = appointment
            print(f"Appointment {appointment_id} booked successfully.\n")
        else:
            print("Patient or Doctor not found.")



    def view_upcoming_appointments(self):

        if len(self.appointments)==0:
            print("There are no upcoming appointments at the moment.")
        
        else:
            print("Upcoming Appointments:")
            for appointment in self.appointments.values():
                print(f"{appointment}\n")

            

    def cancel_appointment(self, appointment_id):
        if appointment_id in self.appointments:
            del self.appointments[appointment_id]
            print(f"Appointment {appointment_id} canceled successfully.")
        else:
            print(f"Appointment {appointment_id} not found.")     