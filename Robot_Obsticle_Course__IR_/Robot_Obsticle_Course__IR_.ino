#include <Servo.h>
int LED = 13; // Use the onboard Uno LED
int isObstaclePin = 7;  // This is our input pin
int isObstacle = HIGH;  // HIGH MEANS NO OBSTACLE
Servo servoRight;
Servo servoLeft;

void moveForward() {
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  delay(1000);
}

void moveBackward() {
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
  delay(1000);
}

void turnLeft(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
  delay(1000);
}

void turnRight(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
  delay(1000);
}

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(isObstaclePin, INPUT);
  Serial.begin(9600);
}

void loop() {
  isObstacle = digitalRead(isObstaclePin);
  if (isObstacle == LOW)
  {
    moveBackward();
    turnLeft();
    moveForward();
    delay(1000);
    
    digitalWrite(LED, HIGH);
  }
  else
  {
    moveForward();
    digitalWrite(LED, LOW);
  }
  delay(200);
}


