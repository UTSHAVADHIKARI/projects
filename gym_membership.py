# Console-based Gym Membership App 

class GymMembershipApp:
    def __init__(self):
        # Dictionary to store members
        # Structure: { member_id: {"name": name, "age": age, "membership": membership_type} }
        self.members = {}
        # Unique ID assigned to each new member
        self.member_id = 1

    def add_member(self, name, age, membership_type):
        """
        Adds a new member with given details.
        Increments member_id after adding.
        """
        self.members[self.member_id] = {
            "name": name,
            "age": age,
            "membership": membership_type
        }
        print(f"✅ Member '{name}' added successfully with ID {self.member_id}!\n")
        self.member_id += 1  # Increment for next member

    def view_members(self):
        """
        Displays all members in the system.
        """
        if not self.members:
            print("⚠️ No members found.\n")
        else:
            print("🏋️ All Gym Members:")
            # Loop through dictionary and print each member
            for mid, details in self.members.items():
                print(f"ID: {mid}, Name: {details['name']}, Age: {details['age']}, Membership: {details['membership']}")
            print()

    def search_member(self, member_id):
        """
        Searches a member by their ID.
        """
        member = self.members.get(member_id)  # Returns None if ID not found
        if member:
            print(f"🔎 Found Member → ID: {member_id}, Name: {member['name']}, Age: {member['age']}, Membership: {member['membership']}\n")
        else:
            print("❌ Member not found!\n")

    def update_membership(self, member_id, new_type):
        """
        Updates membership type for a given member ID.
        """
        if member_id in self.members:
            self.members[member_id]['membership'] = new_type
            print(f"✅ Membership updated for ID {member_id} → {new_type}\n")
        else:
            print("❌ Member not found!\n")

    def delete_member(self, member_id):
        """
        Deletes a member from the system using their ID.
        """
        if member_id in self.members:
            removed = self.members.pop(member_id)  # Remove and return member data
            print(f"🗑️ Member '{removed['name']}' (ID: {member_id}) removed successfully!\n")
        else:
            print("❌ Member not found!\n")


# ------------------ MAIN PROGRAM ------------------ #
def main():
    # Create an instance of GymMembershipApp
    app = GymMembershipApp()
    
    while True:
        # Display menu options
        print("==== Gym Membership App ====")
        print("1. Add Member")
        print("2. View Members")
        print("3. Search Member")
        print("4. Update Membership")
        print("5. Delete Member")
        print("6. Exit")
        
        # Take user choice
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Add a new member
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            membership = input("Enter membership type (Monthly/Quarterly/Yearly): ")
            app.add_member(name, age, membership)
        
        elif choice == "2":
            # View all members
            app.view_members()
        
        elif choice == "3":
            # Search for a member
            member_id = int(input("Enter Member ID to search: "))
            app.search_member(member_id)
        
        elif choice == "4":
            # Update a member's membership
            member_id = int(input("Enter Member ID to update: "))
            new_type = input("Enter new membership type: ")
            app.update_membership(member_id, new_type)
        
        elif choice == "5":
            # Delete a member
            member_id = int(input("Enter Member ID to delete: "))
            app.delete_member(member_id)
        
        elif choice == "6":
            # Exit application
            print("👋 Exiting Gym Membership App. Stay Fit!")
            break
        
        else:
            # Handle invalid input
            print("⚠️ Invalid choice! Please try again.\n")


# Entry point of program
if __name__ == "__main__":
    main()