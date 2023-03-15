import pywhatkit

phone_number = input("enter phone number")
hour = input("enter the hour you want the message to be sent")
minute = input("enter minute you wanted the message to be sent")
pywhatkit.sendwhatmsg(phone_number,"Test",13,51,3,True,3)# this code is for a person

group_id=input("enter group id")


pywhatkit.sendwhatmsg_to_group(group_id,"test",hour,minute,5,True,3)# this one is for a group msg
