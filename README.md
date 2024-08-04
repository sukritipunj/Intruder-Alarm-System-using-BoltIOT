# Intruder-Alarm-System-using-BoltIOT
Security system using Microcontroller : 
an IOT-based program to detect and notify about rogue intruders by creating a circuit using Bolt Microcontroller, LDR and buzzer.

Ensuring the security of homes and businesses is of paramount importance. To address this need, I have developed an IoT-based Intruder Detection System using the Bolt Microcontroller. This project focuses on detecting and notifying about rogue intruders through a comprehensive system that integrates hardware design and cloud-based deployment.

The core of this system is a circuit that I designed with a Light Dependent Resistor (LDR) for precise detection of rogue activity. Upon detection, the system triggers a buzzer alarm and simultaneously sends SMS alert notifications to designated recipients, ensuring immediate awareness of any unauthorized entry. The electronic hardware design was done using Fritzing, while cloud services were leveraged to deploy, and Twilio messaging API to notify about the activity.

By placing the sensor at the entrance of the room under a constant light source such that whenever there are any signs of rogue-activity and a shadow falls on the LDR sensor, the cicuit can easily catch the irregularity and launch the buzzer-alarm through the Bolt Microcontroller and cloud-connection followed by an sms-notification to the user's phone. This system can be deployed to ensure security both in a domestic or an industrial environment.

Hardware Components Used :
   Bolt WiFi Module
   Light Dependent Resistor (LDR)
   Buzzer
   10kohm resister
   Breadboard
   USB cable
   connecting wires (male and female)

Online services Used : 
<img width="89" alt="bolt" src="https://github.com/user-attachments/assets/4e9b4ff5-2e2d-4420-bfec-c234e5527f97">
<img width="148" alt="twilio" src="https://github.com/user-attachments/assets/860b8d90-1185-44f8-965c-cb60015b3cb8">

Hardware Design :
![project schematics](https://github.com/user-attachments/assets/3224c684-d3a4-4203-804e-9ad7c54948a3)

Connections : 
![connections](https://github.com/user-attachments/assets/3a71e5d4-87e8-4aca-a288-528f6238f836)

Bolt Cloud Connection :
<img width="996" alt="cloud connection" src="https://github.com/user-attachments/assets/1b82a9cd-40e8-4e16-bffc-4e8a5c3c1ac1">

SMS Notification :
<img width="350" alt="sms notification" src="https://github.com/user-attachments/assets/0d9ed277-c141-45ed-a7ac-6d5c45bc8a5d">


