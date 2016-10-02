
// Define constants and variables
const int out1 = 5; // define Arduino pin connected to relay 1
const int out2 = 6; // define Arduino pin connected to relay 2
const int out3 = 7; // define Arduino pin connected to relay 3
const int out4 = 8; // define Arduino pin connected to relay 4
int status1, status2, status3, status4;
int message = 0; 




void setup() {
  pinMode(out1, OUTPUT); // initialize the digital pin as an output
  pinMode(out2, OUTPUT); // initialize the digital pin as an output
  pinMode(out3, OUTPUT); // initialize the digital pin as an output
  pinMode(out4, OUTPUT); // initialize the digital pin as an output
  status1 = 0;
  status2 = 0;
  status3 = 0;
  status4 = 0;
  Serial.begin(9600);    // Serial Port initialization

}

// enable or disable a relay (1 to 4)
void setRelay(int relay, int value)
{
  if (relay > 0 && relay < 5) digitalWrite((relay + 4), value);
}

void loop() {
  if (Serial.available())  {
    message = Serial.read() - '0'; // on soustrait le caractère 0, qui vaut 48 en ASCII

    switch (message) {
      case 1:
        if (status1 = 0) {
          setRelay(1, 1);
          status1 = 1;
        } else {
          setRelay(1, 0);
          status1 = 0;
        }

        break;
      case 2:
        if (status2 = 0) {
          setRelay(2, 1);
          status2 = 1;
        } else {
          setRelay(2, 0);
          status2 = 0;
        }
        break;
      case 3:
        if (status1 = 0) {
          setRelay(3, 1);
          status3 = 1;
        } else {
          setRelay(1, 0);
          status3 = 0;
        }
        break;
      case 4:
        if (status4 = 0) {
          setRelay(4, 1);
          status4 = 1;
        } else {
          setRelay(4, 0);
          status4 = 0;
        }
        break;
      default:
        break;
    }
  }
}
