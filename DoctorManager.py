from doctor import Doctor

class DoctorManager:
    def __init__(self):
      self.doctors = [] #create an empty list
      self.read_doctors_file()


    def format_dr_info(self, doctor):
      return f"{doctor.get_doctor_id()}_{doctor.get_name()}_{doctor.get_specialization()}_{doctor.get_working_time()}_{doctor.get_qualification()}_{doctor.get_room_number()}" #format in the txt file


    def enter_dr_info(self):
      docId = input("\nEnter the doctor's ID: ")
      docName = input("Enter the doctor's name: ")
      docSpeciality = input("Enter the doctor's speciality: ")
      docTiming = input("Enter the doctor's timing (e.g., 7am-10pm): ")
      docQual = input("Enter the doctor's qualification: ")
      docRoom = input("Enter the doctor's room number: ")
      return Doctor(docId, docName, docSpeciality, docTiming, docQual, docRoom) #make doctor object using class doctor  


    def read_doctors_file(self):
      with open('doctors.txt') as d:
        self.header = next(d).strip() #take out the first line (header) in the txt file
        for line in d:
          doctor_data = line.strip('\n').split('_')

          if len(doctor_data) == 6: #ensure that there is 6 data for each doctor
            doctor_id, name, specialization, working_time, qualification, room_number = doctor_data

            doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
            self.doctors.append(doctor) #add object to empty list


    def search_doctor_by_id(self):
      findId = input("Enter the doctor Id: ")

      for doctor in self.doctors: 
        if doctor.get_doctor_id() == findId:
          self.display_doctor_info(doctor)
          return
      
      print("Can't find the doctor with the same ID on the system\n")
      return None


    def search_doctor_by_name(self):
      findName = input("Enter the doctor name: ")

      for doctor in self.doctors: 
        if doctor.get_name() == findName:
          self.display_doctor_info(doctor)
          return
      
      print("Can't find the doctor with the same name on the system\n")
      return None


    def display_doctor_info(self, doctor):
      displayLabel = f'\n{"Id":<5}{"Name":<23}{"Speciality":<16}{"Timing":<16}{"Qualification":<16}{"Room Number":<12} \n'
      print(displayLabel)

      displayInfo = f'{doctor.get_doctor_id():<5}{doctor.get_name():<23}{doctor.get_specialization():<16}{doctor.get_working_time():<16}{doctor.get_qualification():<16}{doctor.get_room_number():<12} \n'
      print(displayInfo)


    def edit_doctor_info(self):
      editDoc = input("Please enter the id of the doctor that you want to edit their information: ")

      for doctor in self.doctors:
        if doctor.get_doctor_id() == editDoc:
          doctor.set_name(input("\nEnter new Name: "))
          doctor.set_specialization(input("Enter new Specialist in: "))
          doctor.set_working_time(input("Enter new Timing: "))
          doctor.set_qualification(input("Enter new Qualification: "))
          doctor.set_room_number(input("Enter new Room number: "))
          print(f"\nDoctor whose ID is {doctor.get_doctor_id()} has been edited\n")


          with open('doctors.txt', 'w') as d:
            d.write(self.header + '\n')
            for doctor in self.doctors:
              edit = f'{doctor.get_doctor_id()}_{doctor.get_name()}_{doctor.get_specialization()}_{doctor.get_working_time()}_{doctor.get_qualification()}_{doctor.get_room_number()}\n'
              d.write(edit)

          return doctor
        
      print("Cannot find the doctor …")
      return None

    def display_doctors_list(self):
      displayLabel = f'\n{"Id":<5}{"Name":<23}{"Speciality":<16}{"Timing":<16}{"Qualification":<16}{"Room Number":<12} \n'
      print(displayLabel)

      for doctor in self.doctors:
        displayInfo = f'{doctor.get_doctor_id():<5}{doctor.get_name():<23}{doctor.get_specialization():<16}{doctor.get_working_time():<16}{doctor.get_qualification():<16}{doctor.get_room_number():<12} \n'
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
        d.write('\n' + newFormat)
      print(f"\nDoctor whose ID is {newDoc.get_doctor_id()} has been added\n")