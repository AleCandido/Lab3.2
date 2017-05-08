/* 
 *  Create a traffic light with FSM on arduino
 */
#define SERIALE 0 //se la trasmissione seriale degli stati è abilitata

#define LVstate 0
#define LVGstate 1
#define LRstate 2
#define LOFFstate 3
#define LGstate 4


const int LVpin = 9; // led verde
const int LGpin = 10; // led giallo
const int LRpin = 11; // led rosso
const int ENpin = 8; // input pin for enable

const int timeV = 4000; //time of greeen (ms)
const int timeVG = 1500; //time of verde giallo (ms)
const int timeR = 2000; //time of rosso (ms)
const int timeG =  1500; // time del lampeggiante

int times[4];
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
	//setup tempi...
  times[0]=timeV;  //questo non sarebbe proprio necessario....ma va be!
  times[1]=timeVG;
  times[2]=timeR;
  times[3]=timeG; 
}

void loop() {
  // 1. read the input
  // swith (state) 
  // 2. generate the output
  // 3. calculate the next state
  // 4. wait for this state to complete
  //1.
  inEnable = (digitalRead(ENpin)==HIGH);
 #if SERIALE 
  Serial.println(thisState);
  Serial.println(inEnable);
 #endif 
  stateWait=times[thisState];
  //2.
  setOutput(outputs[thisState]);
  //3.
  if(inEnable) nextState=(thisState+1)%3; //loop fra gli stati 0, 1, 2. se trova 3 va in 1, se trova 4 va in 2
  else nextState=3+ thisState % 2; //loop fra gli stati 3-4. se trova 0 o 2 va in 3, se trova 1 va in 4
  //4.
  delay(stateWait);
  thisState = nextState;
}


int setOutput(int* ordine) {
  int LV=ordine[0];
  int LG=ordine[1];
  int LR=ordine[2];
 #if SERIALE 
  Serial.println("setOutput");
  Serial.print(LV);  
  Serial.print(LG);
  Serial.println(LR);
 #endif 
  digitalWrite(LVpin, LV);  
  digitalWrite(LGpin, LG);
  digitalWrite(LRpin, LR);
}



