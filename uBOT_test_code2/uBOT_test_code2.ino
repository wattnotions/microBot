

int ms_delay = 1500;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
 
 
  a1();
  a2();
  
                   
}

void a1(){
  digitalWrite(2, HIGH);   //step 1
  digitalWrite(3, LOW);
  Serial.println("a1") ; 
  delay(ms_delay);
}

void b1(){
  digitalWrite(4, LOW);   //step 1
  digitalWrite(5, HIGH);  
   Serial.println("b1") ; 
  delay(ms_delay);
}

void a2(){
  digitalWrite(2, LOW);   //step1 
  digitalWrite(3, HIGH);  
   Serial.println("a2")   ; 
  delay(ms_delay);
}

void b2(){
  digitalWrite(4, HIGH);  //step1 
  digitalWrite(5, LOW);   
   Serial.println("b2")  ;
  delay(ms_delay);
}
