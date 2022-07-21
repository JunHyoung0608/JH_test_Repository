module repple_carry_adder_4bit(carry,sum, a, b);
    input [3:0]a;
    input [3:0]b;
    output carry;
    output [3:0]sum;


    assign {carry, sum} = a + b;
endmodule