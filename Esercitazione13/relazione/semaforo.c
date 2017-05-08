/* 
 *  Create a traffic light with FSM on arduino
 */
#define SERIALE 0 //se la trasmissione seriale degli stati è abilitata
#define ENABLE_LOGICAL_HIGH HIGH //per chi volesse invertire la logica dell'enable

//definizione degli stati...non vengono mai usati esplicitamente
#define LVstate 0
#define LVGstate 1
#define LRstate 2
#define LOFFstate 3
#define LGstate 4

#define LVpin  9 // led verde
#define LGpin  10 // led giallo
#define LRpin  11 // led rosso
#define ENpin 8 // input pin for enable

#define timeV  4000 //time of greeen (ms)
#define timeVG  1500 //time of verde giallo (ms)
#define timeR  2000 //time of rosso (ms)
#define timeG   1500 // time del lampeggiante

int pins[4]={LVpin, LGpin, LRpin, ENpin};
int times[4]={timeV, timeVG, timeR, timeG};
int outputs[5][3]={{HIGH, LOW, LOW},{HIGH, HIGH, LOW},{LOW, LOW, HIGH},{LOW, LOW, LOW} , {LOW, HIGH, LOW}}; //tabella degli output in funzione dello stato corrente!!!


int thisState = LOFFstate; // this state
int nextState = LOFFstate; // next state
int stateWait = timeG; // state wait
bool inEnable = false; // enable bit


void setup() {
  pinMode(LVpin, OUTPUT);
  Serial.begin(9600);
  pinMode(LGpin, OUTPUT);
  pinMode(LRpin, OUTPUT);
  pinMode(ENpin, INPUT_PULLUP);
}

void loop() {
  //1. read the input
  inEnable = (digitalRead(ENpin)==ENABLE_LOGICAL_HIGH);
 #if SERIALE 
  Serial.println(thisState);
  Serial.println(inEnable);
 #endif 
  stateWait=times[thisState];
  //2.generate the output
  setOutput(outputs[thisState]);
  //3.calculate the next state
  thisState=UpDate(thisState, inEnable);
  //4. wait for this state to complete
  delay(stateWait);
}


int UpDate(int state, int enable){ //  dato lo stato corrente e il valore di enable da lo stato successivo
  if(inEnable) return (thisState+1)%3; //loop fra gli stati 0, 1, 2. se trova 3 va in 1, se trova 4 va in 2
  else  return 3+ thisState % 2; //loop fra gli stati 3-4. se trova 0 o 2 va in 3, se trova 1 va in 4
}

int setOutput(int* ordine) {
 #if SERIALE 
  Serial.println("setOutput");
  for(int i=0; i<3; i++)
    Serial.println(ordine[i]);
 #endif 
 for(int i=0; i<3; i++)
    digitalWrite(pins[i] , ordine[i]);
}

