class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()
    
    def format_patient_info_for_file(self, patient: "Patient"):
        return "_".join((patient.get_pid(), patient.get_name(), patient.get_disease(), patient.get_gender(), patient.get_age()))

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
                info = line.split("_")
                patient = Patient(info[0], info[1], info[2], info[3], info[4])
                self.patients.append(patient)

    def search_patient_by_Id(self):
        id = input("Enter the Patient Id: ")
        for patient in self.patients:
            if patient.get_pid() == id:
                self.display_patient_info(patient)
                return 
        print("Can't find the patient")        

    def display_patient_info(self, patient: "Patient"):
        print(
            f"{'ID':<5}{'Name':<23}{'Disease':<16}{'Gender':<16}{'Age':<3}\n"
            f"{patient.get_pid():<5}{patient.get_name():<23}{patient.get_disease():<16}{patient.get_gender():<16}{patient.get_age():<3}"
        )
    
    def edit_patient_info_by_id(self):
        pass

    def display_patients_list(self):
        print(f"{'ID':<5}{'Name':<23}{'Disease':<16}{'Gender':<16}{'Age':<3}")
        for patient in self.patients:
            print(f"{patient.get_pid():<5}{patient.get_name():<23}{patient.get_disease():<16}{patient.get_gender():<16}{patient.get_age():<3}")

    def write_list_of_patients_to_file(self):
        pass

    def add_patient_to_file(self):
        newPatient = self.enter_patient_info()
        self.patients.append(newPatient)

        text = self.format_patient_info_for_file(newPatient)
        with open("patients.txt", "a") as file:
            file.write(text)
        
        # TODO confirm new patient as been added
        



# class Patient:
#     def __init__(self, pid, name, disease, gender, age):
#         self.pid = pid
#         self.name = name
#         self.disease = disease
#         self.gender = gender
#         self.age = age

#     def __str__(self) -> str:
#         return "_".join((self.pid, self.name, self.disease, self.gender, self.age))
    

manager = PatientManager()
for patient in manager.patients:
    print(patient)
