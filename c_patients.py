#this is the separate file for the Patients class

#Properties:
# pid, name, disease, gender, age
class Patient:
    def __init__(self, pid = "N/A", name = "N/A", disease = "N/A", gender = "N/A", age = "N/A"):
        self.__pid = pid
        self.__name = name
        self.__disease = disease
        self.__gender = gender
        self.__age = age

    #getters
    def get_pid(self):
        return self.__pid
    
    def get_name(self):
        return self.__name
    
    def get_disease(self):
        return self.__disease

    def get_gender(self):
        return self.__gender
    
    def get_age(self):
        return self.__age
    
    #setters
    def set_pid(self, pid):
        self.__pid = pid 

    def set_name(self, name):
        self.__name = name
    
    def set_disease(self, disease):
        self.__disease = disease

    def set_gender(self, gender):
        self.__gender = gender
    
    def set_age(self, age):
        self.__age = age

    #str return format pid_name_disease_gender_age
    def __str__(self):
        return f"{self.__pid}_{self.__name}_{self.__disease}_{self.__gender}_{self.__age})"
    
# print(Patient())
