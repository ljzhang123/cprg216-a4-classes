#this is the separate file for the Patients class

#Properties:
# pid, name, disease, gender, age
class Patient:
    def __init__(self, pid = "N/A", name = "N/A", disease = "N/A", gender = "N/A", age = "N/A"):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    #getters
    def get_pid(self):
        return self.pid
    
    def get_name(self):
        return self.name
    
    def get_disease(self):
        return self.disease

    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age
    
    #setters
    def set_pid(self, pid):
        self.pid = pid 

    def set_name(self, name):
        self.name = name
    
    def set_disease(self, disease):
        self.disease = disease

    def set_gender(self, gender):
        self.gender = gender
    
    def set_age(self, age):
        self.age = age

    #str
    def __str__(self):
        return f"Patient(pid={self.pid}, name={self.name}, disease={self.disease}, gender={self.gender}, age={self.age})"
