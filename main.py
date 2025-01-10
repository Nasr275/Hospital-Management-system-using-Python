from Modules.my_classes import Doctor, Patient, MedicalRecord
from Modules.HMS import HospitalManagmentSystem , clear



if __name__ == "__main__":

    hms = HospitalManagmentSystem()

    choice = int(input("Welcome to the Hospital Managment System please choose one of the following options:\n1-Patients\n2-Doctors\n3-Appointments\n4-Medical Records\n0-Exit\n"))
    clear()
    exit = False
    while(not exit):

        if choice == 1:
            second_choice = int(input("Choose one of the following patient related options:\n1-Add Patient\n2-Update patient\n3-Delete patient\n4-Search patients\n0-Return\n"))
            clear()

            if second_choice == 1:
                patient_id =  input("ID: ")
                name = input("Enter the name of the patient: ")
                age = int(input("Enter the patient's age: "))
                gender = input("Gender: ")
                contact_info = input("Contact Info: ")
                clear()

                hms.add_patient(patient_id,name,age,gender,contact_info)

            if second_choice == 2:    
                patient_id =  input("Enter the ID of the patient you want to update: ")
                
                name = input("Enter updated name of the patient (Press Enter to leave as defualt): ")
                age = int(input("Enter updated patient's age (Press Enter to leave as defualt): "))
                gender = input("Gender (Press Enter to leave as defualt): ")
                contact_info = input("updated contact Info (Press Enter to leave as defualt): ")
                clear()

                hms.update_patient(patient_id,name,age,gender,contact_info)

            if second_choice == 3:
                patient_id =  input("Enter the ID of the patient you want to delete: ")
                clear()
                
                hms.delete_patient(patient_id)


            if second_choice == 4:
                search_term =  input("Enter either the ID or the name of the patient you want to search for: ")
                clear()

                hms.search_patient(search_term)


            if choice == 0:
                break


        if choice == 2:

            second_choice = int(input("Choose one of the following doctor related options:\n1-Add doctor\n2-Assign patient\n3-Search doctors\n0-Return\n"))
            clear()
            if second_choice == 1:
                doctor_id =  input("ID: ")
                name = input("Enter the name of the Doctor: ")
                age = int(input("Enter the Doctor's age: "))
                gender = input("Gender: ")
                contact_info = input("Contact Info: ")
                clear()

                hms.add_doctor(doctor_id,name,age,gender,contact_info)

            if second_choice == 2:    
                doctor_id =  input("Enter the ID of the doctor to assign a patient to: ")
                patient_id =  input("Enter the ID of the patient you want to assign to a doctor: ")
                clear()

                hms.assign_doctor_to_patient(doctor_id,patient_id)

            if second_choice == 3:
                search_term =  input("Enter either the ID or the name of the doctor you want to search for: ")   
                clear()          
                hms.search_doctor(search_term)


            #if second_choice == 4:




            if choice == 0:
                break


        if choice == 3:
            second_choice = int(input("Choose one of the following appointment related options:\n1-Book appointment\n2-View upcoming appointments\n3-Cancel appointment\n0-Return\n"))
            clear()
            if second_choice == 1:

                appointment_id =  input("Enter the appointment ID: ")
                
                patient_id = input("Patient's ID: ")
                doctor_id = (input("Doctors's ID: "))
                date = input("Date: ")
                time = input("Time: ")
                clear()

                hms.book_appointment(appointment_id, patient_id, doctor_id, date, time)

            if second_choice == 2:
                clear()

                hms.view_upcoming_appointments() 

            if second_choice == 3:
                
                appointment_id =  input("Enter the appointment ID you want to delete: ")
                clear()
                hms.cancel_appointment(appointment_id)                            

            if choice == 0:
                break


        if choice == 4:
            second_choice = int(input("Choose one of the following options:\n1-Add diagnoses\n2-Add medication\n3-Add visit records\n4-View records\n0-Return\n"))
            clear()
            if second_choice == 1:
                patient_id = input("Enter Patient ID: ")
                diagnoses =  input("Enter Patient's diagnosis: ")

                clear()
                hms.patients_dict[patient_id].medical_record.add_diagnosis(diagnoses)
                #globals()[f"patient_{patient_id}"].add_diagnoses(diagnoses)


            if second_choice == 2:
                patient_id = input("Enter Patient ID: ")
                medication = input("Enter Medication: ")
                dosage = input("Enter Dosage: ")
                frequency = input("Enter Frequancy: ")

                clear()
                #globals()[f"patient_{patient_id}"].add_medication(medication, dosage, frequency)
                hms.patients_dict[patient_id].medical_record.add_medication(medication,dosage,frequency)



            if second_choice == 3:
                
                patient_id = input("Enter Patient ID: ")
                visit_record = input("Enter Patient's visit record: ")
                
                clear()
                #globals()[f"patient_{patient_id}"].add_visit_record(visit_record)
                hms.patients_dict[patient_id].medical_record.add_visit_record(visit_record)


            if second_choice == 4:
                
                patient_id = input("Enter Patient ID: ")
        
                
                clear()
                #globals()[f"patient_{patient_id}"].view_records()    
                hms.patients_dict[patient_id].medical_record.view_records()


            if choice == 0:
                break


        if choice == 0:
            break

        leave = input("would you like another service? (y/n): ").lower()
        if leave == 'no' or leave == 'n':
            exit =  True
        else:
            choice = int(input("Please choose one of the followimg options:\n1-Patients\n2-Doctors\n3-Appointments\n4-Medical Records\n0-Exit\n"))
            clear()
        

    print("Thank you for using our HMS, have a nice day!")        
                     











