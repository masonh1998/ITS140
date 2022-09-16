
print ("Reboot the computer and try to connect")
print ("Problem Fixed?")

reboot_1 = (input("Enter yes or no: "))

if reboot_1 == ("yes") :
    print ("Problem fixed")
elif reboot_1 == ("no") :
    print ("Reboot the router and try to connect")

reboot_2 = (input("Problem fixed? Enter yes or no: "))

if reboot_2 == ("yes") :
    print ("Problem fixed")
elif reboot_2 == ("no") :
    print ("Make sure cables between the router and moderm are properly connected.")

reboot_3 = (input("Problem fixed? Enter yes or no : "))

if reboot_3 == ("yes") :
    print ("Problem fixed")
elif reboot_3 == ("no") :
    print ("Move the router to a new location and try to connect.")
    
move_router = (input("Problem fixed? Enter yes or no : "))

if move_router == ("yes") :
    print ("Problem fixed")
elif move_router == ("no") :
    print ("Get a new router.")