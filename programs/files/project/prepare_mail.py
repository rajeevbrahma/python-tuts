import csv          # module which has methods/functions to read and write csv files


# opening two files 
with open("./data/mail_template.txt","r+") as mail_template, open("./data/participants.csv") as participants_file:
    
    # reading lines from the .txt file
    content = mail_template.readlines()

    # reading csv contents using DictReader method
    participants = csv.DictReader(participants_file)
    
    # iterating through all the participants and preparing the certificate
    for participant in participants:

        # We know that the "Hello" is in line number 5
        # preparing the hello message for each participant
        content[5] = content[5][:-1] + participant["name"] + ","        
            
        name = participant["name"]
        # creating certificate file for the participant
        with open(f"./certificates/{name}_course_completion_mail.txt","w") as new_file_name:
            new_file_name.writelines(content)
        
        # resetting the "Hello"
        content[5] = "Hello \n"
        
        
