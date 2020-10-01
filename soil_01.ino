int A = A0;
int w=A1;
int D = 11;
int i;
int j;
int out = LED_BUILTIN;
int x=8;
int y=9;
void setup() {
  // put your setup code here, to run once:
pinMode(A,INPUT);
pinMode(D,OUTPUT);
pinMode(out,OUTPUT);
pinMode(x,OUTPUT);
pinMode(y,OUTPUT);
digitalWrite(x,LOW);
digitalWrite(y,LOW);
pinMode(w,INPUT);
Serial.begin(9600);
}

void loop() {
digitalWrite(D,HIGH);
delay(10);
i=analogRead(A);
//Serial.println(i);
delay(100);
j=map(i,450,1023,1,14);
//Serial.println(j);
//sensor chinese same for indian
if(j>=4)
{
 digitalWrite(y,HIGH);
 digitalWrite(x,LOW);
}
else if(j<4)
{
  
  digitalWrite(x,HIGH);
  digitalWrite(y,LOW);
}
Serial.println(j);
if(analogRead(w)>200){
  digitalWrite(out, HIGH);
}else{
  digitalWrite(out, LOW);
}
}

  /*switch(j)
{
  case 1:digitalWrite(out, LOW);//lv 7
  case 2:digitalWrite(out, LOW);//lv 6
  case 3:digitalWrite(out, LOW);//lv 5
  case 4:digitalWrite(out, HIGH);//lv 4
  case 5:digitalWrite(out, HIGH);//lv 3
  case 7:digitalWrite(out, HIGH);//lv 2
  case 9:digitalWrite(out, HIGH);//lv 1
  case 10:digitalWrite(out, HIGH);//lv 1
  case 11:digitalWrite(out, HIGH);//lv 1
  case 8:digitalWrite(out, HIGH);//lv 1-2
}*/
