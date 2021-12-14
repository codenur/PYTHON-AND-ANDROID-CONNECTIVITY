import time

from ppadb.client import Client as AdbClient

def connect():
    
    client = AdbClient(host="127.0.0.1", port=5037) 

    devices = client.devices()

    if len(devices) == 0:
        
        print('No devices')
        
        quit()

    device = devices[0]
    
    print('Connected to ',devices)
    return device, client


    
if __name__ == '__main__':
    device, client = connect()

    
    device.shell('input keyevent 84')#crome will open
    device.shell('input keyevent 42')#Keyboard Character 'N'
    device.shell('input keyevent 49')#Keyboard Character 'U'
    device.shell('input keyevent 46')#Keyboard Character 'R'
    device.shell('input keyevent 66')#enter
    time.sleep(5)
    device.shell('input keyevent 3')
    print("OPeration done")

    """
    device.shell('input keyevent 5')
    print('Taken a photo!')
    """