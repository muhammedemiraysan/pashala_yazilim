#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4);
int x;

void setup() {
  lcd.init();                     
  lcd.init();
  lcd.backlight();
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available());
  x = Serial.readString().toInt();
  lcd.setCursor(1,0);
  lcd.print(String(x));
  Serial.print(x + 1);
  delay(1000);
  lcd.clear();
}
