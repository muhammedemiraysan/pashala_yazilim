#include <Servo.h>
#include <dht.h>
#include "millisDelay.h" 
#define DHT11_PIN 4
dht DHT;
String inString = ""; int pwmVal = 1450;
byte servoPin = 9; byte servoPin1 = 10; byte servoPin2 = 7; byte servoPin3 = 8; byte servoPin4 = 5; byte servoPin5 = 6;
Servo servo; Servo servo1; Servo servo2; Servo servo3; Servo servo4; Servo servo5; 
millisDelay Delay;
void Run(int pwmVal){servo.writeMicroseconds(pwmVal);}
void Run1(int pwmVal){servo1.writeMicroseconds(pwmVal);}
void Run2(int pwmVal){servo2.writeMicroseconds(pwmVal);}
void Run3(int pwmVal){servo3.writeMicroseconds(pwmVal);}
void Run4(int pwmVal){servo4.writeMicroseconds(pwmVal);}  
void Run5(int pwmVal){servo5.writeMicroseconds(pwmVal);}

void setup() {
  Serial.begin(9600); while (!Serial) {; }
Serial.println("\n\nString toInt():"); Serial.println();
servo.attach(servoPin); servo.writeMicroseconds(1500);
servo1.attach(servoPin1); servo1.writeMicroseconds(1500);
servo2.attach(servoPin2); servo2.writeMicroseconds(1500);
servo3.attach(servoPin3); servo3.writeMicroseconds(1500);
servo4.attach(servoPin4); servo4.writeMicroseconds(1500);
servo5.attach(servoPin5); servo5.writeMicroseconds(1500);
delay(7000);
Delay.start(1000);
}

void loop() {
  
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      inString += (char)inChar;
    }
    if (inChar == '\n') {
      Serial.print("Value:");
      Serial.println(inString.toInt());
      Serial.print("String: ");
      Serial.println(inString);
      pwmVal = inString.toInt();
      inString = "";
    }
  }
  if (Delay.justFinished()) {
    int chk = DHT.read11(DHT11_PIN);
    Serial.print("Temperature = "); Serial.print(DHT.temperature);
    Serial.print(" Humidity = "); Serial.println(DHT.humidity);
    Delay.stop(); Delay.start(1000);
  }
if(pwmVal == 14){Run(1450); Run1(1450); Run2(1450); Run3(1450); Run4(1450); Run5(1450);}
if(pwmVal == 15){Run(1800); Run1(1800); Run2(1800); Run3(1800); Run4(1800); Run5(1800);}
if(pwmVal == 16){Run(1200); Run1(1200); Run2(1200); Run3(1200); Run4(1200); Run5(1200);}
  
//Serial.print(" pwmVal: "); Serial.println(pwmVal);
}
