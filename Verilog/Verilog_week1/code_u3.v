//--------------------주석 종류--------------------
// 한 줄 주석
/*
여러줄 주석
*/

//--------------------연산자--------------------
a=~b; //~는 단항 연산자, B는 피연산자
a=b && c; //&&는 이항 연산자, b와c는 피연산자
a=b ? c : d; //?:는 삼항 연산자, b, c와 d는 피연산자

//--------------------수 표현--------------------
//크기 지정 가능 수
//<크기>'<기본형식><숫자>의 형식을 갖는다.

4'b1111 //4 비트 2진수
12'hbc //12 비트 16진수
16'd255 //16 비트 10진수

//크기 지정 불가능 수
//<기본형식> 지정하지 않을 경우 : 10 진수
//<크기>가 지정 되지 않을 경우 : 32비트
23456 //32 비트 10진수
'hc3 //32 비트 16진수
'o21 //32 비트 8진수

//X,Z값
//X : 알 수 없는 값
//Z : 하이 임피던스 값
//16진수에서 X 또는 Z는 4개의 비트를 정하고, 8진수는 3개의 비트, 2진수에서는 1개의 비트를 정한다.
12'h13x //12 비트 16진수; 마지막 4개 비트는 알 수 없는 값이다.
6'hx //6 비트 16진수
32'bz //32 비트 2진수; 하이 임피던스값이다.

//음수
//음수는 숫자의 <크기> 앞에 음수 보로를 붙인다.
-6'd3 //3의 2의 보수로써 음수
-6'sd3 //부호 있는 정수 계산에 사용

//언더스코어 문자와 물음표
12'd1111_0000_1010 //가독성을 높이기 위해 언더스코어 문자를 사용.
4'b10?? //4'b10zz와 동일.

//--------------------문자열--------------------
"hello Verilog World" //문자열
"a / b" //문자열

//--------------------식별자와 키워드--------------------
reg value; //reg는 키워드. value는 식별자
input clk; //input는 키워드. clk는 식별자

//--------------------에스케이프 식별자--------------------
//에스케이프 식별자는 백슬러쉬(\) 문자로 시작, 화이트스페이스(스페이스, 탭, 개행)로 끝남.
//에스케이프와 화이트 스페이스 사이에 있는 모든 문자들은 글자 그대로 처리 된다.
\a+b-c
\**my_name**

//--------------------논리 값 집합--------------------
//논리 값 :0, 1, x, z
/*신호강도(아래로 갈수록 낮아짐)
supply  흐름(driving) 
strong  흐름(driving) 
pull    흐름(driving) 
large   저장(storage)
week    흐름(driving) 
medium  저장(storage)
small   저장(storage)
highz   하이 임피던스
*/

//--------------------넷(Nets)--------------------
//넷은 하드웨어 요소 사이에 연결을 나타낸다.
wire a; //회로에서 넷 a를 정의
wire b,c; //회로에서 넷 b, c를 정의
wire d= 1'b0 // 넷 d는 논리값 0으로 선언

//--------------------레지스터--------------------
//레지스터는 데이터를 저장할 수 있는 변수이다.
//키워드 : reg 기본 논리 값 : x
reg reset; //값을 가질 수 있는 변수 reset 정의
initial 
begin
    reset = 1'b1 //디지털 회로에서 reset을 1로 초기화 한다.
    #100 reset = 1'b0; //100단위시간이 지난 뒤 reset값을 바꾼다.
end
reg signed [63:0] m; //64 비트 부호 있는 값
initial i; //32 비트 부호 있는 값

//--------------------벡터--------------------
//넷과 reg 데이터형은 벡터로 선언될 수 있다.
//벡터는 항상 왼쪽에 있는 것이 최상위 비트를 나다낸다.
wire a; //스칼라 넷 변수. 기본 값.
wire [7:0] bus; //8-비트 bus.
wire [31:0] busA, busB, busC; //32-비트의 폭을 가진 3개의 bus들.
reg clock; //스칼라 레지스터. 기본 값.
reg [0:40] virtural_addr; //41비트 폭을 가진 벡터 레지스터.

//벡터 부분 선택
busA[7]; //벡터 busA의 7번 비트.
bus[2:0] //벡터 bus의 3개의 하위 비트, significant 비트는 범위지정에서 항상 왼쪽에 와야 되기 때문에 bus[0:2]로 사용하는 것은 안된다.
virtual_addr[0:1] //virtual_addr의 2개의 상위 비트.

//가변 벡터 부분 선택
/*
[<시작 비트>+:폭]-시작비트부터 부분 선택 증가
[<시작 비트>-:폭]-시작비트부터 부분 선택 감소
*/
reg [255:0] data1; //리틀-엔디언(Little endian) 표기법
reg [0:255] data2; //빅-엔디언(Big endian) 표기법
reg [7:0] byte;
//가변 부분 선택을 사용, 각각은 부분들을 선택할 수 있다.
byte = data1[31-:8]; //시작비트 : 31, 폭 : 8 -> data[31:24]
byte = data1[24+:8]; //시작비트 : 24, 폭 : 8 -> data[31:24]
byte = data2[31-:8]; //시작비트 : 31, 폭 : 8 -> data[24:31]
byte = data2[24+:8]; //시작비트 : 24, 폭 : 8 -> data[24:31]
/*
시작비트는 변할 수 있다. 폭은 상수 값을 가진다
그러므로, 루프문을 이용하여 벡터의 모든 바이트들을
선택하기 위하여 가변 부분 선택을 사용할 수 있다.
*/
for (j=0; j<=31; j=j+1)
    byte = data1[(j*8)+8]; //순서는 [7:0], [15:8] ... [255:248]
//벡터의 부분을 초기화할 수 있다.
data1[(byteNum*8)+:8] = 8'b0; //만약  btyeNum = 1, 8 비트 [15:8]를 클리어.

//--------------------정수, 실수, 시간 레지스터 데이터형--------------------
//정수 
//키워드 : integer
//범용 변수로 reg를 사용해도 되지만 카운트 같은 목적은 위해서는 정수를 사용하는 것이 더 편하다.
integer counter; //counter로 사용되는 범용 변수.
initial
    counter=-1; //counter에 음수 1을 저장.

//실수
//키워드 : real
/*
실수는 십진표기법(3.14) 또는 과학적 표기법(3e6)으로 나타낼 수 있다.
실수는 벡터를 가질 수 없고, 기본값은 0이다. 실수가 정수로 대입될 때, 실수는 반올림된다.
*/
real delta; //delta라는 실수를 정의.
initial
begin
    delta = 4e10; //delta에 과학적 표기법으로 대입.
    delta = 2.13; //delta에 2.13을 대입.
end
integer i; //정수 i를 정의.
initial
    i = delta; //i는 2값을 갖는다(2.13의 변환값).
//시간
//키워드 : time
/*
Verilog 시뮬레이션은 시뮬레이션 시간을 고려하면서 동작한다.
시간 레지스터 데이터형의 폭은 기계에 따라서 지덩된다. 그러나 적어도 64-비트이다.
시스템 함수 $time은 현재의 시뮬레이션 시간을 얻고자 할 때 쓴다.
*/
time save_sim_time; //시간변수 save_sim_time을 정의.
initial
    save_sim_time=$time; //현재 시뮬레이션 시간을 저장.

//--------------------배열--------------------
//형태 : <배열 이름>[<서브스크립트>]
integer count[0:7]; //8 count 변수의 배열.
reg bool[31:0]; //32 1-비트 boolean 레지스터 변수의 배열.
time chk_point[1:100]; //100 time chk_point 변수의 배열.
reg [4:0] port_id[0:7]; //8 port_id의 배열; 각port_id는 5-비트의 폭을 가진다.
integer matrix[4:0][0:225]; //정수령 이차원 배열.
reg [63:0] array_4d [15:0][7:0][7:0][225:0]; //사차원 배열.
wire w_array1[7:0][5:0] //싱글 비트 와이어의 배열 선언.
/*
넷또는 레지스터 벡터와 배열을 혼동하지 않는 것이 중요하다.
벡터는 n-비트의 폭을 가지는 하나의 원소이다. 반며에 배열은 1-비트 또는 n-비트를 가지는 여러 원소이다.
*/
coount[5] = 0; //count 변수 배열의 5번째 원소 리셋.
chk_point[100] = 0; //check point 값이 100번째 시간 리셋.
port_id[3] = 0; //port_id 배열의 세번째 원소 리셋. 5-비트 값이다.
matrix[1][0] = 33559; //[1][0]인덱스의 원소 값을 33559로 셋.
array_4d[0][0][0][15:0] = 0; //[0][0][0][0] 색인에 의해 접근되어지는 레지스터의 15:0 비트들을 클리어.

//--------------------메모리--------------------
/*
Verilog에서 메모리는 단순히 레지스터의 배열로 만들어진다.
배열의 각 원소는 워드이다. 각 워드는 1 또는 여러 비트가 될 수 있다.
1-비트 레지스터와 1개의 n-레지스터를 구분하는 것은 중요하다. 
메모리에서 부분적인 워드는 주소로 사용되어서 메모리 배열 서브스크립트로 간주된다.
*/
reg mem1bit[0:1023]; //메모리 mem1bit는 1k 1-비트 워드를 가진다.
reg [7:0]membyte[0:1023]; //메모리membyte는 1k 8-비트 워드(바이트)를 가진다.
membyte[511] //주소가 511인 1바이트 워드를 나타낸다.

//--------------------파라미터--------------------
//키워드 : parameter
/*
파라미터는 변수로 사용할 수 없다. 각 모듈 인스턴스의 파라미터값은 컴파일 시 개별적으로 대치된다.
이러한 방법으로 모듈 인스턴스를 개별적으로 조정할 수 있다.
*/
parameter port_id=5; //상수 port_id를 정의한다.
parameter cache_line_width = 256; //캐쉬 줄의 폭을 정의한 상수.
parameter signed [15:0] WIDTH; //파라미터 WIDTH에 대한 부호와 범위 고정
/*
Verilog 로컬 파라미터(키워드 localparam으로 정의되는)는 
defparam 문장 혹은 정룔돈 혹은 이름 지어진 파라미터 값 할당에 의해 직접적인 조작할 수 없는 파라미터이다.
localparam 키워드는 파라미터 값이 변해서는 안될 때 사용한다.
*/
localparam state1 = 4'b0001,
           state2 = 4'b0010,
           state3 = 4'01000,
           state4 = 4'10000;

//--------------------문자열--------------------
/*
문자열은 reg에 저장 될 수 있다. 레지스터 변수의 폭은 문자열을 저장할 수 있을만큼 커저야한다.
문자열의 각 문자는 8-비트(1-바이트)를 처리한다.
*/
reg [8*18:1] string_value; //18-바이트의 폭을 갖는 변수 선언.
initial
    string_value = "Hello Verilog World"; //변수에 문자열 저장.

//--------------------시스템 태스크--------------------
/*
Verilog는 루틴 연산을 하기 워한 표준 시스템 태스크(Standard system task)를 제공한다.
모든 시스템 태스크는 $<키워드> 형태로 나타낸다.
시스템 태스크에 의한 연산은 화면에 출력하고, 넷의 값을 모니터링하고, 멈추고, 끝내는 것들이다.
*/
//화면 출력 태스크
//$display는 변수의 값 또는 문자열 또는 수식을 출력하기 위한 주요 시스템 태스크이다.
//사용법 : $display(p1, p2, p3, ..., pn);
/*
display의 형식은 C의 printf와 매우 유사하다.
$display는 어떤 인자 없이 개행을 수행한다.
*/
//따옴표 안의 문자열을 출력.
$display("Hello Verilog World");
//현재 시뮬레이션 시간 230을 출력.
$display($time);
//41-비트 virtual address의 값 1fe0000001c 그리고 시간 200을 출력.
reg [0:40] virtual_addr;
$display("At time %d virtual address is %h",$time, virtual_addr);
//port_id 값 5를 2진수로 출력.
reg [4:0] port_id; $display("ID of the port is %b", port_id);
//x문자를 출력.
//4-비트 bus의 값 10xx(신호 충돌)을 2진수로 출력.
reg [3:0] bus; $display("Bus value is %b", bus);
//최상위 top 모듈에서 파생된 인스턴스 p1의 계층 이름을 출력.
//인자가 필요하지 않다. 유요한 특징이다.
$display("This string is display from %m levl of hierarchy");
//특수 문자 개행과 %의 출력.
$display("This is a \n multiline string with a %% sign");

//모니터링 태스크
//$monitor 태스크로 신호값이 변할 때마다 그 신호를 출력할 수 있다.
//사용법 : $monitor(p1, p2, p3, ..., pn);
/*
$monitor 태스크를 사용하는 것은 $display 태스크를 사용하는 것과 비슷하다.
$monitor는 변수 또는 파라미터에 지정된 신호의 값을 계속 모니터링하고, 
리스트의 어느 한 변수나 신호가 변할 때마다 모든 파라미터를 출력한다.
$display와 달리, $monitor는 단 한번만 사용할 필요가 있다. 동시에 단 하나의 모니터링 리스트만 수행된다.
만약 하나 이상의 $minitor문장이 시뮬레이션에 존재하면, 마지막 $monitor 문장이 수행될 것이다.
*/

//사용법 : $monitoron;
//         $monitoroff;
/*
$monitoron 태스크는 시뮬레이션하는 동안 모니터링을 할 수 있게 하고,
$monitoroff 태스크는 모니터링을 할 수 없게 한다.
모니터링은 시뮬레이션을 시작할 때는 기본으로 on 상태이고, 시뮬레이션이 진행되는 동안 $monitoron과 $monitoroff 태스크를 사용해 조절할 수 있다.
*/
//시간과 클럭 그리고 리셋 신호의 값을 모니터링.
initial
begin
    $mointor($time, "Value of siganls clock = %b reset = %b", clock, reset);
end

//시뮬레이션의 중단과 종료 태스크
//시뮬레이션을 하는 동안 중단을 하기 위해서 태스크 $stop를 제공한다.
//사용법 : $stop;
/*
$stop 태스크는 상호 작용 모드의 시뮬레이션에서 사용된다 설계자는 상호작용모드를 통해서 디버그를 할 수 있다.
$stop 태스크 설계자가 시뮬레이션 중단을 원하거나 신호의 값을 조사하고자 할 때마다 사용할 수 있다.
*/
//사용법 : $finsh;
//단위 시간 100에 시뮬레이션을 중단하고 결과를 조사.
initial
begin
    clock = 0;
    reset = 1;
    #100 $stop; //단위 시간 100에 시뮬레이션을 중단.
    #900 $finish; //단위 시간 1000에 시뮬레이션을 끝냄.
end

//'difine
/*
`dfine 지시어는 Verilog에서 텍스트 매크로를 정의하는데 사용한다.
Verilog 컴파일러는 `<매크로 이름>을 만나면 매크로의 텍스트로 대치한다.
이것은 C에서 #difine과 유사하다.
*/
//기본 워드 크기를 텍스트 매크로로 정의.
//코드 내에서 'WORD_SIZE로 사용.
`define WORD_SIZE 23
//별명을 정의. `S가 나타날 때마다 $stop로 대치.
`difine S $stop;
//자주 사용되는 텍스트 문자열을 정의.
`difine WORD_REG reg [31:0]
// `WORD_REG reg32;로 32-비트 레지스터를 정의할 수 있다.

//`include
/*
`include 지시어는 다른 Verilog 파일에 있는 Verilog 소스 파일의 전체 내용을 컴파일 하는 동안 포함하게 해준다.
이 작업은 C의 #include와 유사하다.
*/
//main 파일인 design.v 파일에서 header.v 파일을 포함
`include header.V