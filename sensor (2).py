import adafruit_dht
import time
import board
import smtplib

dht_device = adafruit_dht.DHT22(board.D22)

user = 'handclap.thewalker@gmail.com'
password = 'Pooh1bear'

while True:
    try:
        temp = dht_device.temperature
        tempf = temp * (9/5) + 32
        hum = dht_device.humidity
        if tempf > 80:
            try:
                smtp = smtplib.SMTP('smtp.gmail.com', 587)

                smtp.starttls()
                smtp.login("onepiecetreasureseis@gmail.com", "ofbfqrgrefxbutky")

                message = "Temp is higher than 80 degrees fahrenheit!"

                smtp.sendmail("onepiecetreasureseis@gmail.com", user, message)

                smtp.quit()
                print("email sent")
            except Exception as error:
                print("an error has occured", error)

        print("temp: {:.1f}F   humidity = {}%".format(tempf, hum))
        break
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dht_device.exit()
        raise error
    finally:
        time.sleep(5.0)
        dht_device.exit()
