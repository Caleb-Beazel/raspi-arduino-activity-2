//send temp
// receive data from serial --> power on/off LED
#define LED_PIN 13

unsigned long lastTimeTempSent = millis();
unsigned long tempSentDelay = 1000;

void setup() {
  Serial.begin(115200);
  while(!Serial) {}
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  unsigned long timeNow = millis();
  if (timeNow - lastTimeTempSent >= tempSentDelay) {
    lastTimeTempSent = timeNow;
    int temperature = random(5,25);
    Serial.println(temperature);
  }

  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    if (cmd == "on") {
      digitalWrite(LED_PIN, HIGH);
    }
    else if (cmd == "off"){
      digitalWrite(LED_PIN, LOW);
    }
    else{
      
      }
  }



}
