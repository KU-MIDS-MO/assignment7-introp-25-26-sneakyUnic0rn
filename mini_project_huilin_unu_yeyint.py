# ==================================================
# Group Members:
# 1. Ye Yint
# 2. Huilin
# 3. Unu
#
# System Description:
# Campus Facility Booking System
#
# Additional Features:
# - Duplicate facility prevention
# - Partial search
# - Booking / status tracking
# - History / activity log

# ==================================================

# Main data storage (nested list)
facilities = [["Meeting Room", 15, "Available"], ["Boardgame Room", 10, "Available"], ["Lecture Theatre", 100, "Available"]]
activity_log = []

# ---------------- RETURN TO MENU --------------
def back_to_menu():
    input("\nPress Enter to return to menu...")

def add_log(message):
    activity_log.append(message)
  
# ---------------- ADD FACILITY ----------------
def add_facility():
    name = input("Enter facility name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    # Duplicate check
    for facility in facilities:
        if facility[0].lower() == name.lower():
            print("Facility already exists.")
            return

    try:
        capacity = int(input("Enter capacity: "))
        if capacity <= 0:
            print("Capacity must be positive.")
            return
    except ValueError:
        print("Invalid capacity.")
        return

    status = "Available"
    facilities.append([name, capacity, status])
    print("Facility added successfully.")
    add_log(f"Added facility: {name}, capacity={capacity}")

# ---------------- VIEW FACILITIES ----------------
def view_facilities():
    if len(facilities) == 0:
        print("No facilities available.")
        return

    print("\nFacilities:")
    #for i in range(len(facilities)):
    for i, facility in enumerate(facilities):
        print(f"{i + 1}. Name: {facility[0]}, Capacity: {facility[1]}, Status: {facility[2]}")


# ---------------- SEARCH FACILITY ----------------
def search_facility():
    if len(facilities) == 0:
        print("No facilities available.")
        return

    keyword = input("Enter search keyword: ").lower()
    found = False

    for facility in facilities:
        if keyword in facility[0].lower():
            print(f"Name: {facility[0]}, Capacity: {facility[1]}, Status: {facility[2]}")
            found = True

    if not found:
        print("No matching facility found.")
    add_log(f"Searched facility with keyword: {keyword}")


# ---------------- UPDATE FACILITY ----------------
def update_facility():
    if len(facilities) == 0:
        print("No facilities available.")
        return

    view_facilities()

    try:
        choice = int(input("Select facility number to update: "))
        if choice < 1 or choice > len(facilities):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    facility = facilities[choice - 1]

    print("\n1. Update name")
    print("2. Update capacity")
    print("3. Update status")

    try:
        option = int(input("Choose option: "))
    except ValueError:
        print("Invalid input.")
        return

    if option == 1:
        new_name = input("Enter new name: ").strip()
        old_name = facility[0]
        facility[0] = new_name
        print("Name updated.")
        add_log(f"Updated facility name: {old_name} -> {new_name}")
    elif option == 2:
        try:
            new_capacity = int(input("Enter new capacity: "))
            if new_capacity > 0:
                facility[1] = new_capacity
                print("Capacity updated.")
                add_log(f"Updated capacity of {facility[0]} to {new_capacity}")
        except ValueError:
            print("Invalid capacity.")
    elif option == 3:
        facility[2] = "Available" if facility[2] == "Booked" else "Booked"
        print("Status updated.")
        add_log(f"Changed status of {facility[0]} to {facility[2]}")
    else:
        print("Invalid option.")


# ---------------- DELETE FACILITY ----------------
def delete_facility():
    if len(facilities) == 0:
        print("No facilities available.")
        return

    view_facilities()

    try:
        choice = int(input("Select facility number to delete: "))
        if choice < 1 or choice > len(facilities):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    confirm = input("Are you sure? (y/n): ").lower()
    if confirm == "y":
        removed=facilities.pop(choice - 1)
        print("Facility deleted.")
        add_log(f"Deleted facility: {removed[0]}")
    else:
        print("Deletion cancelled.")


# ---------------- BOOKING / STATUS ----------------
def manage_booking():
    if len(facilities) == 0:
        print("No facilities available.")
        return

    view_facilities()

    try:
        choice = int(input("Select facility number: "))
        if choice < 1 or choice > len(facilities):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    facility = facilities[choice - 1]

    if facility[2] == "Available":
        facility[2] = "Booked"
        print("Facility booked.")
        add_log(f"Booked facility: {facility[0]}")
    else:
        facility[2] = "Available"
        print("Booking cancelled.")
        add_log(f"Cancelled booking: {facility[0]}")

# ---------------- MENU ----------------
def view_activity_log():
    if len(activity_log) == 0:
        print("No activity recorded yet.")
    else:
        print("\n--- Activity Log ---")
        for i, log in enumerate(activity_log, start=1):
            print(f"{i}. {log}")

# ---------------- SUMMARY REPORT------------------
def summary_report():
    if len(facilities) == 0:
        print("No facilities available.")
        return
    total = len(facilities)
    booked = 0
    available = 0
    
    report_lines = []
    report_lines.append("\nFacility Booking Summary Report\n")
    
    for facility in facilities:
        if facility [2] == "Booked":
            booked += 1 
        else:
            available += 1 
    
    booking_percentage = (booked / total) * 100
    
    report_lines.append(f"Total facilities     : {total}\n")
    report_lines.append(f"Available facilities : {available}\n")
    report_lines.append(f"Booked facilities    : {booked}\n")
    report_lines.append(f"Booking percentage   : {booking_percentage:.2f}%\n\n")
    
    report_lines.append("Booked Facility Details: \n")
    
    has_booking = False
    for facility in facilities:
        if facility[2] == "Booked":
            report_lines.append(f"- {facility[0]} (Capacity: {facility[1]}, Booked by: {facility[2]})\n")
            has_booking = True
    if not has_booking:
        report_lines.append("No active bookings. \n")
    
    # print report to screen
    print("". join(report_lines))
    
    # export to text file
    with open("summary_report.txt", "w") as file:
        file.writelines(report_lines)
    print("Summary report exported to 'summary_report.txt'")

# ---------------- MENU ----------------
def menu():
    while True:
        print("\n====== Campus Facility Booking System ======")
        print("1. Add facility")
        print("2. View facilities")
        print("3. Search facility")
        print("4. Update facility")
        print("5. Delete facility")
        print("6. Manage booking")
        print("7. View activity log")
        print("8. Summary report")
        print("9. Exit")


        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            add_facility()
            back_to_menu()
        elif choice == 2:
            view_facilities()
            back_to_menu()
        elif choice == 3:
            search_facility()
            back_to_menu()
        elif choice == 4:
            update_facility()
            back_to_menu()
        elif choice == 5:
            delete_facility()
            back_to_menu()
        elif choice == 6:
            manage_booking()
            back_to_menu()
        elif choice == 7:
            view_activity_log()
            back_to_menu()
        elif choice == 8:
            summary_report()
            back_to_menu()
        elif choice == 9:
            print("Thank you for using the system.")
            break
        else:
            print("Invalid menu choice.")


# ---------------- PROGRAM START ----------------
menu()
