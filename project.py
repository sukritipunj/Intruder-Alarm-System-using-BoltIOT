import json, time, config

from boltiot import Bolt,Sms

my_BoltModule= Bolt(config.API_KEY,config.DEVICE_ID)      


def on_buzzer() :
    return_value_on= my_BoltModule.digitalWrite("0","HIGH")

    return return_value_on

def off_buzzer() :
    return_value_off=my_BoltModule.digitalWrite("0","LOW")

    return return_value_off

def readLDR() :
    print("Please Wait...")
    print("^^^Currently reading LDR value^^^")
    
    inp_info=my_BoltModule.analogRead("A0")
    data=json.loads(inp_info)
    
    print("The LDR value corresponds to : "+ str(data["value"]))

    return data

def messageAlert(value) :
    
    sms = Sms(config.SID, config.AUTH_TOKEN, config.TO_NUMBER, config.FROM_NUMBER)
    
    print("Making request to Twilio to send a SMS")
    
    response1 = sms.send_sms("The LDR value is "+str(value))
    response2 = sms.send_sms(" System Compromised!! ")
    
    print("Response received from Twilio is: " + str(response1))
    print(str(response2))
    print("Status of SMS at Twilio is :" + str(response1.status))
    


        

first_data=readLDR()

first_value=int(first_data["value"])

while True :
    time.sleep(7)
    second_data=readLDR()
    second_value=int(second_data['value'])
    

    if first_value>second_value :
        on_buzzer()
        print("   buzzer buzzes because LDR is",second_value)
        messageAlert(second_value)
        time.sleep(7)
        off_buzzer()

    first_value=second_value

    
