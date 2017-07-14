#include <Servo.h>

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
  servoLeft.attach(13);
  servoRight.attach(12);
}

void loop() {
  moveForward();
  turnRight();
 
}
