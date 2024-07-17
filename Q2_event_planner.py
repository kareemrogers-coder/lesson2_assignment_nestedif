###Question2

## Objective To practice the use of shorthand if statements in determining event-related decisions.

### Task1 Code Correction

###You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

####BUGGY CODE:

""" attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > 100 elif "conference room"
print(venue) """

#####BELOW IS THE CORRECTED VERSION:

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

print("="*50)
print("="*50)

##Task 2: Catering Choices

###Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

attendees = int(input("Enter number of attendees: "))

print("large hall" if attendees >= 100 else "conference room")

caterers_selector = input(" Would you like a vegetarian option yes or no? ")
if caterers_selector == "yes":
    print("Veggie Delight Caterers")
elif caterers_selector == "no":
    print ("Gourmet Meals Caterers")
else:
    print("invalid answer.. program terminated")
