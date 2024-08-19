from DoctorManager import DoctorManager
from pManager import PatientManager

class Management:
    def display_menu(self):
        while True:
            mainMenuSelect = input(
                "Welcome to Alberta Hospital (AH) Managment system\n"
                "Select from the following options, or select 3 to stop:\n"
                "1 - 	Doctors\n"
                "2 - 	Patients\n"
                "3 -	Exit Program\n"
            )

            if mainMenuSelect == "1":
                manager = DoctorManager()
                while True:
                    dMenuSelect = int(input(
                        "\nDoctors Menu:\n"
                        "1 - Display Doctors list\n"
                        "2 - Search for doctor by ID\n"
                        "3 - Search for doctor by name\n"
                        "4 - Add doctor\n"
                        "5 - Edit doctor info\n"
                        "6 - Back to the Main Menu\n"
                    ))

                    match dMenuSelect:
                        case 1:
                            manager.display_doctors_list()
                        case 2:
                            manager.search_doctor_by_id()
                        case 3:
                            manager.search_doctor_by_name()
                        case 4:
                            manager.add_dr_to_file()
                        case 5:
                            manager.edit_doctor_info()
                        case 6:
                            print()
                            break
                        case _:
                            print("Please enter a valid option")


            elif mainMenuSelect == "2":
                manager = PatientManager()
                while True:
                    pMenuSelect = int(input(
                        "\nPatients Menu:\n"
                        "1 - Display patients list\n"
                        "2 - Search for patient by ID\n"
                        "3 - Add patient\n"
                        "4 - Edit patient info\n"
                        "5 - Back to the Main Menu\n"
                    ))
                    
                    match pMenuSelect:
                        case 1:
                            manager.display_patients_list()
                        case 2:
                            manager.search_patient_by_Id()
                        case 3:
                            manager.add_patient_to_file()
                        case 4:
                            manager.edit_patient_info_by_id()
                        case 5:
                            print()
                            break
                        case _:
                            print("Please enter a valid option")
            
            elif mainMenuSelect == "3":
                print("Thanks for using the program. Bye!")
                break




a = Management()
a.display_menu()