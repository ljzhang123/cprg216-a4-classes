#Class Doctor
class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    # Getters
    def get_doctor_id(self):
        return self.doctor_id
    
    def get_name(self):
        return self.name
    
    def get_specialization(self):
        return self.specialization
    
    def get_working_time(self):
        return self.working_time
    
    def get_qualification(self):
        return self.qualification
    
    def get_room_number(self):
        return self.room_number

    #setters
    def set_doctor_id(self, doctor_id):
        self.doctor_id = doctor_id
    
    def get_name(self, name):
        self.name = name
    
    def get_specialization(self, specialization):
        self.specialization = specialization
    
    def get_working_time(self, working_time):
        self.working_time = working_time
    
    def get_qualification(self, qualification):
        self.qualification = qualification
    
    def get_room_number(self, room_number):
        self.room_number = room_number

    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"
        