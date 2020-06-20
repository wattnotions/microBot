

int ms_delay = 25;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  
  digitalWrite(2, LOW);   //step1 
  digitalWrite(3, HIGH);  

  digitalWrite(6, LOW);   
  digitalWrite(7, HIGH);    
  delay(ms_delay);    

  digitalWrite(4, HIGH);  //step1 
  digitalWrite(5, LOW);   

  digitalWrite(8, LOW);   
  digitalWrite(9, HIGH);    
  delay(ms_delay);

  digitalWrite(2, HIGH);   //step 1
  digitalWrite(3, LOW);    

  digitalWrite(6, HIGH);   
  digitalWrite(7, LOW);    
  delay(ms_delay); 

  digitalWrite(4, LOW);   //step 1
  digitalWrite(5, HIGH);  

  digitalWrite(8, HIGH);   
  digitalWrite(9, LOW);    
  delay(ms_delay);
                   
}
