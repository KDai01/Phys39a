

void setup() {
  Serial.begin(9600);
}

void loop() {
  int inputPotent = analogRead(A1);
  int outputPotent = map(inputPotent, 0, 1023, 0, 255);
  analogWrite(6,outputPotent);
  delay(50);
}
