#include "Arduino.h"
#include "Magnets.h"

coilSystem::coilSystem(int mosfetPin, int irLEDpin, int photoPin, int photoAnalogpin, int photoValue, int beamSystemleds, int mosfetLED)
{
  pinMode(mosfetPin, OUTPUT);
  pinMode(irLEDpin, OUTPUT);
  pinMode(photoPin, OUTPUT);
  pinMode(beamSystemleds, OUTPUT);
  pinMode(mosfetLED, OUTPUT);
  digitalWrite(mosfetPin, LOW);
  digitalWrite(irLEDpin, LOW);
  digitalWrite(photoPin, LOW);
  digitalWrite(beamSystemleds, LOW);
  digitalWrite(mosfetLED, LOW);
  
  _mosfetPin = mosfetPin;
  _irLEDpin = irLEDpin;
  _photoPin = photoPin;
  _photoAnalogpin = photoAnalogpin;
  _photoValue = photoValue;
  _mosfetLED = mosfetLED;
  _beamSystemleds = beamSystemleds;
}

void coilSystem::on()
{
  digitalWrite(_mosfetPin, HIGH);
  digitalWrite(_irLEDpin, HIGH);
  digitalWrite(_photoPin, HIGH);
}

int coilSystem::analogReadingreturn()
{
  _photoValue = 0;
  _photoValue = analogRead(_photoAnalogpin);
  return _photoValue;

}

void coilSystem::analogReading_serialPrint()
{
  unsigned long time;
  time = millis();
  Serial.begin(9600);
  Serial.print(_photoValue);
  Serial.print(",");
  Serial.println(time);
  Serial.end();
}

void coilSystem::off()
{
  digitalWrite(_mosfetPin, LOW);
  digitalWrite(_irLEDpin, LOW);
  digitalWrite(_photoPin, LOW);
}

//checks
void coilSystem::analogReadingcheck()
{
  _photoValue = 0;
  _photoValue = analogRead(_photoAnalogpin);
  delay(1000);
  _photoValue = 0;
  _photoValue = analogRead(_photoAnalogpin);
  if(_photoValue <= 1000 || _photoValue <= 500)
  {
   Serial.begin(9600);
   Serial.println("NO ANLOG READING");
   Serial.println(_photoValue);
   Serial.end();
  }
  else
  { 
   Serial.begin(9600);
   Serial.println("BEAM SYSTEM FUNCTIONAL");
   Serial.println(_photoValue);
   Serial.end();
  }
}
//checks
void coilSystem::coilSystemcheck()
{
  if(digitalRead(_irLEDpin) == HIGH && digitalRead(_photoPin) == HIGH)
  {
   Serial.begin(9600);
   Serial.println("BEAM SYSTEM PINS FUNCTIONAL");
   Serial.end();
  }
  else
  {
   if(digitalRead(_irLEDpin) == LOW)
   {
    Serial.begin(9600);
    Serial.println("IR LED PIN NOT WORKING");
    Serial.end();
   }
   delay(2000);
   if(digitalRead(_photoPin) == LOW)
   {
    Serial.begin(9600);
    Serial.println("PHOTOTRANSISTOR NOT WORKING");
    Serial.end();
   }
 }
 delay(2000);
 digitalWrite(_mosfetPin, HIGH);
 if(digitalRead(_mosfetPin) == LOW)
 {
  Serial.begin(9600);
  Serial.println("MOSFET NOT WORKING");
  Serial.end();
 }
 digitalWrite(_mosfetPin, LOW);
}

void coilSystem::beamSystemon()
{
  digitalWrite(_beamSystemleds, HIGH);
}

void coilSystem::mosfetOn()
{
  digitalWrite(_mosfetLED, HIGH);
}

void coilSystem::beamSystemoff()
{
  digitalWrite(_beamSystemleds, LOW);
}

void coilSystem::mosfetOff()
{
  digitalWrite(_mosfetLED, LOW);
}