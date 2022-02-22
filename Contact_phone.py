##****** write data in matrix********
counter = 0
class contact:
    # def list of data
    plist = list()

    # ***************start menu****************
    def start_menu(x):
        if x.lower() == 'start':
            ans=True
            while ans:
                print("1.Add a contact\n2.Delete a contact\n3.Look Up contact\n4.Save Data to CSV file\n5.Read CSV file\n6.Exit/Quit")
                print(f"Number of contacts: {len(plist)}")
                ans=input("")
                if ans=="1": print("\nAdd a contact"); addstudent()
                elif ans=="2": print("\n Delete a contact"); delstudent()
                elif ans=="3": print("\n Look Up contact"); findstudent()
                elif ans=="4": print("\n Save Data to CSV file"); savetotext()
                elif ans=="5": print("\n Read CSV file"); csvreader()
                elif ans=="6": print("\n Goodbye"); break
                elif ans !="": print("\n Not Valid Choice Try again")
        else: print("Ok Bye :))")
    # function for add student part 1
    def addstudent():
        i = True
        while i is True:
            pdic = {}
            pdic["First Name"] = input("First Name ")
            pdic["Last Name"] = input("Last Name ")
            pdic["Phone Number"] = input("Phone Number ")
            pdic["Email Address"] = input("Email Address ")
            pdic["Birthday"] = input("Birthday (ex. year/month/day ) ")
            pdic["Address"] = input("Address ")
            pdic["Social Profile Url"] = input("Social Profile Url ")
            #for key, value in pdic.items(): print(key,value,":","\n")
            add = input("Add contact? (yes or no) / for main menu type back")
            if add.lower() == 'yes' : i=False; plist.append(pdic)
            if add.lower() == 'back': i=False
            plist.sort(key= lambda x: x[1])
    # function for Delete a contact part 2
    def delstudent():
        print(plist)
        loser = str(input("who do you want to delete? "))
        counter = 0
        for k in plist:
            counter +=1
            for key, value in k.items():
                if loser == value:
                    print("exist")
                    print(k)
                    return print("exist")
            if  counter == len(plist): print("contact doesn't exist")




    # function for Look Up contact part 3
    #def findstudent():

    # function of saving SCV file part 4
    def savetotext():
        import csv
        header = ['First Name', 'Last Name', 'Email Address', 'Birthday','Address','Social Profile Url']
        with open('contact.csv','w', encoding='UTF8') as file:
            writercsv = csv.writer(file)
            writercsv.writerow(header)
            for i in plist:
                writercsv.writerow(i.values()) # write value of dic in the list to csv
            file.close()
        print("Data Saved as contaxt.csv in directory.")
    # function for Read CSV file part 5
    #def csvreader():


#************RUN*****************
contact.start_menu(input("write start to see the menu :)^"))
