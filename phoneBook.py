import sys
import os

class Contact():    
    
    def __init__(self, surname, first_name, phone_number):
        self.surname=surname
        self.first_name=first_name
        self.phone_number=phone_number


    def contact_exists(self, n_entries):
    #method to search if a contact already exists on the phoneBook    
        first=False
        sur=False
        
        if n_entries>0:
            try:
                file=open("phoneBook","r")
                for line in file.readlines():
                    for l in line.split("\n"):
                        word=l.split(";")
                        for i in word:
                            if i.lower()==self.surname.lower():
                                sur=True
                            elif i.lower()==self.first_name.lower() and sur==True:
                                first=True
                            elif i==self.phone_number and first==True:
                                return True
                            
            except Exception:
                print("It's not possible to read the file")
                
            else:
                file.close()
                return False

    
    def add_contact(self, contact_to_add):
        #method to add contact in the phoneBook
        
        if contact_to_add=="":
            contact_to_add=self.surname+";"+self.first_name+";"+self.phone_number
        
        
        data="\r\n%s" %contact_to_add #to add the line at the end of the file
        
        
        try:
            file=open("phoneBook","a")
            file.write(data)
            return True
        except Exception:
            print("It's not possible to write on the file")
            return False
        else:
            file.close()
    
    def delete_contact(self):
        #method to delete the contact
        
        line_to_delete=self.surname+";"+self.first_name+";"+self.phone_number
        name="Phone_Book"
        
        try:        
            new_file=open(name, 'a') #if the file does not exist creates it

            with open('phoneBook') as old_file:
                for line in old_file:
                    if ((line.rstrip()).lower() != line_to_delete.lower()):
                        new_file.write(line)

           
            new_file.close() #using with is not need to close the file

            os.remove("phoneBook")
            os.rename("Phone_Book", "phoneBook")
            return True
                
        except Exception:
            print("It's not possible to read the file")
            print(Exception)
            return False
        else:
            return False
    
    def edit_contact(self, phone_number):
        contact_to_add=self.surname+";"+self.first_name+";"+phone_number
        
        if(self.delete_contact()):
            if(self.add_contact(contact_to_add)):
                return True
            else:
                return False
        

def treatFiles():
    
    try:
        file=open("phoneBook", "r")
    except IOError:
        print("Can't find the file.")
        return False
    else:
        return True
    
    file.close()

def count_entries():
    
    try:
        file=open("phoneBook", "r")
        rows=sum(1 for line in file)  
    except IOError:
        return -1
    else:
        return rows

def main():
    
    file=treatFiles()
    n_entries=count_entries()
    print(n_entries)
    if file==True:
        action=input("Please choose what you want to do:\n 1 - Add contact \n 2 - Search contact \n 3 - Edit contact \n 4 - Delete contact \n\n 0-Exit ")
    
    
        while (action<"0" or action>"4"):
            action=input("Please choose what you want to do:\n 1 - Add contact \n 2 - Search contact \n 3 - Edit contact \n 4 - Delete contact \n\n 0-Exit ")

        if action==0:
            sys.exit()
        else:
            surname=input("Surname:")
            first_name=input("First_name:")
            phone_number=input("Phone Number:")
            
            contact=Contact(surname, first_name, phone_number)
          
            if action=="1":#Add Contact
                
                if(contact.contact_exists(n_entries)):
                    print("Contact already exists")
                    sys.exit()
                else:
                    if(contact.add_contact("")):
                        print("Contact added successfully!")
                        sys.exit()
                    else:
                        print("It was not possible to add the contact")
                        sys.exit() 
            
            elif action=="2": #Search contact
                if(contact.contact_exists(n_entries)):
                    print("Contact has been found!")
                    print("\nSurname:%s\nFirst name:%s\nPhone Number:%s\n" %(contact.surname, contact.first_name, contact.phone_number))
                else:
                    print("The contact you want to search doesn't exist")
               
            elif action=="3": #Edit Contact
                
                if(contact.contact_exists(n_entries)):
                    new_phone=input("Please insert new Phone Number:")
                    if(contact.edit_contact(new_phone)):
                        print("Contact has been updated successfully!")
                    else:
                        print("It was not possible to edit the contact")
                else:
                    print("This contact doesn't exist.")
                    sys.exit()
                
            elif action=="4": #Delete Contact
                if(contact.contact_exists(n_entries)):
                    if(contact.delete_contact()):
                        print("Contact has been deleted successfully!")
                        sys.exit()
                    else:
                        print("It was not possible to remove the contact")
                else:
                    print("This contact doesn't exist")
    else:  
        print("There is no file with addresses")

if __name__=="__main__":
    main()

