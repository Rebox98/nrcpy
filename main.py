from nrcpy import NrcDevice


ip='192.168.1.200'
port=23
username="admin"
password="admin"


nrc=NrcDevice((ip,port,username,password))
# Open Connection
nrc.connect()

# Login
if nrc.login():
    # Commands
    nrc.relayContact(1,500)
    nrc.relayContact(2,1000)
    nrc.relayOff(1)
    nrc.relayOn(2)
    print("Relays Status (hex):" ,nrc.getRelaysValues())
    print("Relay 1 Status:" ,nrc.getRelayValue(1))
    print("Relay 2 Status:" ,nrc.getRelayValue(2))

    try: 
        print("SW Inputs Status:" ,nrc.getSwInputsValues())
        print("SW 1 Status:" ,nrc.getSwInputValue(1))
        print("SW 2 Status:" ,nrc.getSwInputValue(2))
        print("SW 3 Status:" ,nrc.getSwInputValue(3))
    except Exception as e: 
        print("SW Inputs Status:" ,e)

    try: 
        print("HV Inputs Status:" ,nrc.getHvInputsValues())
        print("HV 1 Status:" ,nrc.getHvInputValue(1))
        print("HV 2 Status:" ,nrc.getHvInputValue(2))
        print("HV 3 Status:" ,nrc.getHvInputValue(3))
    except Exception as e: 
        print("HV Inputs Status:" ,e)
else:
    print("Error in login")

nrc.disconnect()