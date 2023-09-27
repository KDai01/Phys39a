const int thermistorPin = A0;
const int numReadings = 1000;

const float referenceResistor = 100000.0;  // Assuming a 100kΩ resistor for voltage division
const float B = 4540.0;                  // B coefficient of the thermistor
const float R25 = 100000.0;                // Resistance at 25°C
const float TR = 298.15;                 // 25°C in Kelvin
const float RInfinity = R25 * exp(-B / TR);
const float tStart = millis();

void setup() {
  Serial.begin(9600);
  
}

void loop() {
  
  // With Averaging
  long sum = 0;
  for(int i = 0; i < numReadings; i++) {
    sum += analogRead(thermistorPin);
    delay(1);
  }
  float avgReading = (float)sum / numReadings;
  float tEnd = millis();
  float durationSeconds = (millis() - tStart) / 1000.0;  // Calculate duration and convert to seconds

  
  float thermVolt = avgReading*5.0/1023.0 ;
  float resV = 5.0 - thermVolt;
  float curr = resV / referenceResistor;
  float resistance = thermVolt / curr;

  // Calculate temperature using the provided equation
  float temperatureKelvin = B / log(resistance / RInfinity);
  float temperatureCelsius = temperatureKelvin - 273.15; // Convert Kelvin to Celsius

  // Print the results
  // Serial.print("Duration (s): ");
  Serial.print(durationSeconds, 2);
  Serial.print(","); // Temperature (°C): ");
  Serial.println(temperatureCelsius, 2);

  delay(10);
}
