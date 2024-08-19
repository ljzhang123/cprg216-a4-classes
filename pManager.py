from c_patients import Patient

class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()
    
    def format_patient_info_for_file(self, patient: "Patient"):
        return str(patient)

    def enter_patient_info(self) -> "Patient":
        pid = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")

        return Patient(pid, name, disease, gender, age)

    def read_patients_file(self):
        with open("patients.txt", "r") as file:
            header = file.readline()
            for line in file:
                info = line.strip("\n").split("_")
                patient = Patient(info[0], info[1], info[2], info[3], info[4])
                self.patients.append(patient)

    def search_patient_by_Id(self):
        id = input("\nEnter the Patient Id: ")
        for patient in self.patients:
            if patient.get_pid() == id:
                self.display_patient_info(patient)
                return 
        print("Can't find the Patient with the same id on the system")        

    def display_patient_info(self, patient: "Patient"):
        print(
            f"\n{'ID':<5}{'Name':<23}{'Disease':<16}{'Gender':<16}{'Age':<3}\n"
            f"\n{patient.get_pid():<5}{patient.get_name():<23}{patient.get_disease():<16}{patient.get_gender():<16}{patient.get_age():<3}"
        )
    
    def edit_patient_info_by_id(self):
        id = input("Please enter the id of the Patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.get_pid() == id:
                newName = input("Enter new name: ")
                newDisease = input("Enter new disease: ")
                newGender = input("Enter new gender: ")
                newAge = input("Enter new age: ")

                patient.set_name(newName)
                patient.set_disease(newDisease)
                patient.set_gender(newGender)
                patient.set_age(newAge)

                # overwrite entire txt file with new info
                self.write_list_of_patients_to_file()

                print(f"Patient whose ID is {id} has been edited.")
                return
            
        print("Can't find the Patient with the same id on the system")

    def display_patients_list(self):
        print(f"{'ID':<5}{'Name':<23}{'Disease':<16}{'Gender':<16}{'Age':<3}")
        for patient in self.patients:
            print(f"\n{patient.get_pid():<5}{patient.get_name():<23}{patient.get_disease():<16}{patient.get_gender():<16}{patient.get_age():<3}")

    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            file.write("id_Name_Disease_Gender_Age")

            patients = []
            for patient in self.patients:
                patients.append(self.format_patient_info_for_file(patient))

            file.writelines(patients)

    def add_patient_to_file(self):
        newPatient = self.enter_patient_info()
        self.patients.append(newPatient)

        text = self.format_patient_info_for_file(newPatient)
        with open("patients.txt", "a") as file:
            file.write(text)
        
        print(f"Patient whose ID is {newPatient.get_pid} has been added.")
        

    

# manager = PatientManager()
# for patient in manager.patients:
#     print(str(patient))

# print(manager.__dict__["patients"][1].__dict__.values())
