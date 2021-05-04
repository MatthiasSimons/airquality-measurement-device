""""added measure() function to library- M.Simons"""

"""Micropython library for dealing with MQ135 gas sensor
Based on Arduino Library developed by G.Krocker (Mad Frog Labs)
and the corrections from balk77 and ViliusKraujutis
More info:
    https://hackaday.io/project/3475-sniffing-trinket/log/12363-mq135-arduino-library
    https://github.com/ViliusKraujutis/MQ135
    https://github.com/balk77/MQ135
"""

import math
import time
from machine import ADC

class MQ135(object):
    """ Class for dealing with MQ13 Gas Sensors """
    # The load resistance on the board
    RLOAD = 10.0
    # Calibration resistance at atmospheric CO2 level
    RZERO = 76.63
    # Parameters for calculating ppm of CO2 from sensor resistance
    PARA = 116.6020682
    PARB = 2.769034857

    # Parameters to model temperature and humidity dependence
    CORA = 0.00035
    CORB = 0.02718
    CORC = 1.39538
    CORD = 0.0018
    CORE = -0.003333333
    CORF = -0.001923077
    CORG = 1.130128205

    # Atmospheric CO2 level for calibration purposes
    ATMOCO2 = 397.13


    def __init__(self, pin):
        self.pin = pin

    def get_correction_factor(self, temperature, humidity):
        """Calculates the correction factor for ambient air temperature and relative humidity
        Based on the linearization of the temperature dependency curve
        under and above 20 degrees Celsius, asuming a linear dependency on humidity,
        provided by Balk77 https://github.com/GeorgK/MQ135/pull/6/files
        """

        if temperature < 20:
            return self.CORA * temperature * temperature - self.CORB * temperature + self.CORC - (humidity - 33.) * self.CORD

        return self.CORE * temperature + self.CORF * humidity + self.CORG

    def get_resistance(self):
        """Returns the resistance of the sensor in kOhms // -1 if not value got in pin"""
        adc = ADC(self.pin)
        value = adc.read()
        if value == 0:
            return -1

        return (1023./value - 1.) * self.RLOAD

    def get_corrected_resistance(self, temperature, humidity):
        """Gets the resistance of the sensor corrected for temperature/humidity"""
        return self.get_resistance()/ self.get_correction_factor(temperature, humidity)

    def get_ppm(self):
        """Returns the ppm of CO2 sensed (assuming only CO2 in the air)"""
        return self.PARA * math.pow((self.get_resistance() / self.RZERO), -self.PARB)

    def get_corrected_ppm(self, temperature, humidity):
        """Returns the ppm of CO2 sensed (assuming only CO2 in the air)
        corrected for temperature/humidity"""
        return self.PARA * math.pow((self.get_corrected_resistance(temperature, humidity)/ self.RZERO), -self.PARB)

    def get_rzero(self):
        """Returns the resistance RZero of the sensor (in kOhms) for calibratioin purposes"""
        return self.get_resistance() * math.pow((self.ATMOCO2/self.PARA), (1./self.PARB))

    def get_corrected_rzero(self, temperature, humidity):
        """Returns the resistance RZero of the sensor (in kOhms) for calibration purposes
        corrected for temperature/humidity"""
        return self.get_corrected_resistance(temperature, humidity) * math.pow((self.ATMOCO2/self.PARA), (1./self.PARB))
    def measure(self, temperature, humidity):
        correction_factor =  self.get_correction_factor(temperature, humidity)
        resistance = self.get_resistance()
        corrected_resistance = self.get_corrected_resistance(temperature, humidity)
        ppm= self.get_ppm()
        corrected_ppm = self.get_corrected_ppm(temperature, humidity)
        r_zero = self.get_rzero()
        corrected_rzero = self.get_corrected_rzero(temperature, humidity)
        return {"ppm": ppm, "corrected_ppm": corrected_ppm}



def mq135lib_example():
    """MQ135 lib example"""
    # setup
    temperature = 21.0
    humidity = 25.0

    mq135 = MQ135(0) # analog PIN 0

    # loop
    while True:
        rzero = mq135.get_rzero()
        corrected_rzero = mq135.get_corrected_rzero(temperature, humidity)
        resistance = mq135.get_resistance()
        ppm = mq135.get_ppm()
        corrected_ppm = mq135.get_corrected_ppm(temperature, humidity)

        print("MQ135 RZero: " + str(rzero) +"\t Corrected RZero: "+ str(corrected_rzero)+
              "\t Resistance: "+ str(resistance) +"\t PPM: "+str(ppm)+
              "\t Corrected PPM: "+str(corrected_ppm)+"ppm")
        time.sleep(0.3)

if __name__ == "__main__":
    mq135lib_example()


# """Micropython library for dealing with MQ135 gas sensor
# Based on Arduino Library developed by G.Krocker (Mad Frog Labs)
# and the corrections from balk77 and ViliusKraujutis
# More info:
#     https://hackaday.io/project/3475-sniffing-trinket/log/12363-mq135-arduino-library
#     https://github.com/ViliusKraujutis/MQ135
#     https://github.com/balk77/MQ135
# """
#
#
# import math
# from machine import ADC
#
# RLOAD = 10.0
# # Calibration resistance at atmospheric CO2 level
# RZERO = 76.63
# # Parameters for calculating ppm of CO2 from sensor resistance
# PARA = 116.6020682
# PARB = 2.769034857
#
# # Parameters to model temperature and humidity dependence
# CORA = 0.00035
# CORB = 0.02718
# CORC = 1.39538
# CORD = 0.0018
# CORE = -0.003333333
# CORF = -0.001923077
# CORG = 1.130128205
#
#
# # Atmospheric CO2 level for calibration purposes
# ATMOCO2 = 397.13
#
#
# def get_resistance():
#     # MQ135
#     adc = ADC(0)
#     value = adc.read()
#
#     return value
#
# def get_ppm():
#     """Returns the ppm of CO2 sensed (assuming only CO2 in the air)"""
#     return PARA * math.pow((get_resistance() / RZERO), -PARB)
#
# def get_correction_factor(temperature, humidity):
#     if temperature < 20:
#         return CORA * temperature * temperature - CORB * temperature + CORC - (humidity - 33.) * CORD
#
#     return CORE * temperature + CORF * humidity + CORG
#
# def get_corrected_resistance(temperature, humidity):
#     """Gets the resistance of the sensor corrected for temperature/humidity"""
#     return get_resistance()/ get_correction_factor(temperature, humidity)
#
# def get_corrected_ppm(temperature, humidity):
#     """Returns the ppm of CO2 sensed (assuming only CO2 in the air)
#     corrected for temperature/humidity"""
#     return PARA * math.pow((get_corrected_resistance(temperature, humidity)/ RZERO), -PARB)
#
# def get_rzero():
#     """Returns the resistance RZero of the sensor (in kOhms) for calibratioin purposes"""
#     return get_resistance() * math.pow((ATMOCO2/PARA), (1./PARB))
#
# def get_corrected_rzero(temperature, humidity):
#     """Returns the resistance RZero of the sensor (in kOhms) for calibration purposes
#     corrected for temperature/humidity"""
#     return get_corrected_resistance(temperature, humidity) * math.pow((ATMOCO2/PARA), (1./PARB))
#
# def measureMQ135(temperature, humidity):
#     return get_corrected_ppm(temperature, humidity)