//리플 캐리 카운터라는 최상위 블록을 저으이한다.
//이것은 4개의 T-플립플롭을 파생한다.
module ripple_carry_counter (q, clk, reset);

output [3:0] q; 
input clk, reset;

//4개의 T_FF 모듈의 인스턴스가 생성된다. 각 인스턴스는 고유한 이름을 가지고 있다.
//각 인스턴스는 T_FF 모듈의 복사본임을 명심해라.
T_FF tff0 (q[0], clk, reset);
T_FF tff1 (q[1], q[0], reset);
T_FF tff2 (q[2], q[1], reset);
T_FF tff3 (q[3], q[2], reset);

endmodule

//T_FF 모듈을 정의한다. 이것은 하나의 D-플립플롭에서 파생된다. D-플립플롭 모듈은 정의되었다고 가정하자.
module T_FF (q, clk, reset);

output q;
input clk, reset;
wire d;

D_FF dff0 (q, d, clk, reset); //D_FF의 파생이고, 이 인스턴스의 이름은 diff0이다.
not n1 (q, d); //not 게이트는 Verilog의 프리미티브이다.

endmodule

//모듈 D_FF는 동기식 reset를 가지고 이ㅛ다.
module D_FF (q, d, clk, reset);

output q;
input d, clk, reset;
reg q;

always @(posedge reset or negedge clk)
if (reset)
    q <= 1'b0;
else
    q <= d;

endmodule

