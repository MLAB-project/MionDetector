#define horni_fotonasobic  A0
#define dolni_fotonasobic A1 
#define threshold_horni 15
#define threshold_dolni 15
#define reset_1 0
#define reset_2 1
#define led 16

unsigned long mioncounter = 0;

void setup()
{
  Serial.begin(9600);

  pinMode(horni_fotonasobic, INPUT);
  pinMode(dolni_fotonasobic, INPUT);

  pinMode(reset_1, INPUT);
  pinMode(reset_2, INPUT);
  digitalWrite(reset_1, LOW);
  digitalWrite(reset_2, LOW);

  pinMode(led, OUTPUT);
}

void loop()
{
  int signal_horni = analogRead(horni_fotonasobic);
  int signal_dolni = analogRead(dolni_fotonasobic);

  if((signal_horni > threshold_horni) && (signal_dolni > threshold_dolni))
  {
    digitalWrite(led, HIGH);

    mioncounter++;
    Serial.printf("Mion te neminul!|%ld\n", mioncounter);

    delay(50);
    digitalWrite(led, LOW);
  }

  pinMode(reset_1, OUTPUT);
  pinMode(reset_2, OUTPUT);
  digitalWrite(reset_1, HIGH);
  digitalWrite(reset_2, HIGH);
  delay(1);
  pinMode(reset_1, INPUT);
  pinMode(reset_2, INPUT);
  digitalWrite(reset_1, LOW);
  digitalWrite(reset_2, LOW);

  delay(10);
}