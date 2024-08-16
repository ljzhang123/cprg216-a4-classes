class DoctorManager:
    def __init__(self):
      self.doctors = [] #create an empty list
      self.read_doctors_file()


    def format_dr_info(self, doctor):
      formatInfo = f"{doctor.doctor_id}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}" #format in the txt file
      return formatInfo


    def enter_dr_info(self):
      docId = input("\nEnter the doctor's ID: ")
      docName = input("Enter the doctor's name: ")
      docSpeciality = input("Enter the doctor's speciality: ")
      docTiming = input("Enter the doctor's timing (e.g., 7am-10pm): ")
      docQual = input("Enter the doctor's qualification: ")
      docRoom = input("Enter the doctor's room number: ")
      docInfo = Doctor(docId, docName, docSpeciality, docTiming, docQual, docRoom) #make doctor object using class doctor
      return docInfo


    def read_doctors_file(self):
      with open('doctors.txt') as d:
        self.header = next(d).strip() #take out the first line (header) in the txt file
        for line in d:
          doctor_data = line.strip().split('_')

          if len(doctor_data) == 6: #ensure that there is 6 data for each doctor
            doctor_id, name, specialization, working_time, qualification, room_number = doctor_data

            doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
            self.doctors.append(doctor) #add object to empty list


    def search_doctor_by_id(self):
      findId = input("Enter the doctor Id: ")

      for doctor in self.doctors: 
        if doctor.doctor_id == findId:
          return doctor
      
      print("Can't find the doctor with the same ID on the system\n")
      return None


    def search_doctor_by_name(self):
      findName = input("Enter the doctor name: ")

      for doctor in self.doctors: 
        if doctor.name == findName:
          return doctor
      
      print("Can't find the doctor with the same name on the system\n")
      return None


    def display_doctor_info(self, doctor):
      displayLabel = f'\n{"Id":<5}{"Name":<23}{"Speciality":<16}{"Timing":<16}{"Qualification":<16}{"Room Number":<12} \n'
      print(displayLabel)

      displayInfo = f'{doctor.doctor_id:<5}{doctor.name:<23}{doctor.specialization:<16}{doctor.working_time:<16}{doctor.qualification:<16}{doctor.room_number:<12} \n'
      print(displayInfo)


    def edit_doctor_info(self):
      editDoc = input("Please enter the id of the doctor that you want to edit their information: ")

      for doctor in self.doctors:
        if doctor.doctor_id == editDoc:
          doctor.name = input("\nEnter new Name: ")
          doctor.specialization = input("Enter new Specialist in: ")
          doctor.working_time = input("Enter new Timing: ")
          doctor.qualification = input("Enter new Qualification: ")
          doctor.room_number = input("Enter new Room number: ")
          print(f"\nDoctor whose ID is {doctor.doctor_id} has been edited\n")


          with open('doctors.txt', 'w') as d:
            d.write(self.header + '\n')
            for doctor in self.doctors:
              edit = f'{doctor.doctor_id}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}\n'
              d.write(edit)

          return doctor
        
      print("Cannot find the doctor …")
      return None

    def display_doctors_list(self):
      displayLabel = f'\n{"Id":<5}{"Name":<23}{"Speciality":<16}{"Timing":<16}{"Qualification":<16}{"Room Number":<12} \n'
      print(displayLabel)

      for doctor in self.doctors:
        displayInfo = f'{doctor.doctor_id:<5}{doctor.name:<23}{doctor.specialization:<16}{doctor.working_time:<16}{doctor.qualification:<16}{doctor.room_number:<12} \n'
        print(displayInfo)


    def write_list_of_doctors_to_file(self):
      with open('doctors.txt', 'w') as d:
        d.write(self.header + '\n')
        
        for doctor in self.doctors:
          formatInfo = self.format_dr_info(doctor)
          d.write(formatInfo + '\n')


    def add_dr_to_file(self):
      newDoc = self.enter_dr_info()
      self.doctors.append(newDoc)

      newFormat = self.format_dr_info(newDoc)
      with open('doctors.txt', 'a') as d:
        d.write(newFormat + '\n')
      print(f"\nDoctor whose ID is {newDoc.doctor_id} has been added\n")