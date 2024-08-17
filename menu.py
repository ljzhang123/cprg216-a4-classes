class Management:
    def display_menu(self):
        mainMenuSelect = input(
            "Welcome to Alberta Hospital (AH) Managment system\n"
            "Select from the following options, or select 3 to stop:\n"
            "1 - 	Doctors\n"
            "2 - 	Patients\n"
            "3 -	Exit Program\n"
        )

        if mainMenuSelect == "1":
            dMenuSelect = input(
                "\nDoctors Menu:\n"
                "1 - Display Doctors list\n"
                "2 - Search for doctor by ID\n"
                "3 - Search for doctor by name\n"
                "4 - Add doctor\n"
                "5 - Edit doctor info\n"
                "6 - Back to the Main Menu\n"
            )

        elif mainMenuSelect == "2":
            pMenuSelect = input(
                "\nPatients Menu:\n"
                "1 - Display patients list\n"
                "2 - Search for patient by ID\n"
                "3 - Add patient\n"
                "4 - Edit patient info\n"
                "5 - Back to the Main Menu\n"
            )


a = Management()
a.display_menu()