import adafruit_dht
import time
import board
import smtplib

#Can replace D22 with the GPIO number of the pin you connected the sensor to
dht_device = adafruit_dht.DHT22(board.D22)

#Replace with the email you want to receive alerts
user = 'ries.thorsten@gmail.com'

while True:
    try:
        temp = dht_device.temperature
        tempf = temp * (9/5) + 32
        hum = dht_device.humidity
        if tempf > 80:
            try:
                smtp = smtplib.SMTP('smtp.gmail.com', 587)

                smtp.starttls()
                #user and app password for the email address that is sending
                smtp.login("onepiecetreasureseis@gmail.com", "ofbfqrgrefxbutky")

                #Message in the alert
                message = "Temp is higher than 80 degrees fahrenheit!"

                smtp.sendmail("onepiecetreasureseis@gmail.com", user, message)

                smtp.quit()
                print("email sent")
            except Exception as error:
                print("An error has occured", error)

        print("temp: {:.1f}F   humidity = {}%".format(tempf, hum))
        
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dht_device.exit()
        raise error
    finally:
        time.sleep(5.0)
        #dht_device.exit()
