#ifndef coilSystem_h
#define coilSystem_h

#include "Arduino.h"

class coilSystem
{
  public:
    coilSystem(int mosfetPin, int irLEDpin, int photoPin, int photoAnalogpin, int photoValue, int beamSystemleds, int mosfetLED);
    void on();
    int analogReadingreturn();
    void analogReading_serialPrint();
    void off();
    void analogReadingcheck();
    void coilSystemcheck();
    void beamSystemon();
    void mosfetOn();
    void beamSystemoff();
    void mosfetOff();



  private:
    int _beamSystemleds;
    int _mosfetLED;
    int _mosfetPin;
    int _irLEDpin;
    int _photoPin;   
    int _photoAnalogpin;
    int _photoValue;
};
#endif
