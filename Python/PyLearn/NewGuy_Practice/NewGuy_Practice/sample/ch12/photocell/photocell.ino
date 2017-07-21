// 柯博文老師 www.powenko.com 
int ledPin = 13;
int analogPin = 0;
int val = 0;
void setup(){
  Serial.begin(9600);
       pinMode(ledPin, OUTPUT);
}
void loop(){
       val = analogRead(analogPin);
       Serial.println(val);
        if (val <= 100) {
                digitalWrite(ledPin, HIGH); // 當太暗時，led持續發亮
        } else {
                digitalWrite(ledPin, HIGH); // 當有光時，led閃爍
                delay(300);
                digitalWrite(ledPin, LOW);
                delay(300);
        }
       delay(300);
}


