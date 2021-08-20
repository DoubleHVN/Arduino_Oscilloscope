int t = 0;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
}



void loop() {
  for (t=0;t<360;t++) {
    float y1 = 1+ sin( PI/180 * t + 0);
    float y2 =  sin( 9*PI/180 * t + 2);

    Serial.print("y1:");
    Serial.print(y1);
    Serial.print(",");
    Serial.print("y2:");
    Serial.println(y2);
  }
}
