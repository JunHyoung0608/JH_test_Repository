module carry_look_ahead_adder_4bit(carry, a, b);
    input [3:0]a;
    input [3:0]b;
    output [4:0]carry;

    assign carry = (a & b) << 1; //a=1 b=0 c=1? 
endmodule