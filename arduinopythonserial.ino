int datafromUser=0;
void setup() {
  // put your setup code here, to run once:
  pinMode( 3 , OUTPUT );
  pinMode( 4 , OUTPUT );
  pinMode( 5 , OUTPUT );
  pinMode( 6 , OUTPUT );
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    datafromUser=Serial.read();
  }

  if(datafromUser == '1')
  {
    digitalWrite( 3 , HIGH );
    digitalWrite( 4 , LOW );
    digitalWrite( 5 , HIGH );
    digitalWrite( 6 , LOW );
  }
  else if(datafromUser == '0')
  {
    digitalWrite( 3 , LOW );
    digitalWrite( 4 , HIGH );
    digitalWrite( 5 , LOW );
    digitalWrite( 6 , HIGH );
  }
  else if(datafromUser == '2')
  {
    digitalWrite( 3 , LOW );
    digitalWrite( 4 , LOW );
    digitalWrite( 5 , LOW );
    digitalWrite( 6 , LOW );
  }
   else if(datafromUser == '3')
  {
    digitalWrite( 3 , HIGH );
    digitalWrite( 4 , LOW );
    digitalWrite( 5 , LOW );
    digitalWrite( 6 , HIGH );
  }
   else if(datafromUser == '4')
  {
    digitalWrite( 3 , LOW );
    digitalWrite( 4 , HIGH );
    digitalWrite( 5 , HIGH );
    digitalWrite( 6 , LOW );
  }
  
}
