module testbench();
  reg [3:0]a;
  reg [3:0]b;
  wire carry;
  wire [3:0]sum;

  repple_carry_adder_4bit ag(carry, sum, a, b);

  initial begin
    a = 4'b0000; b = 4'b0000;
    #50 a = 4'b0001; b = 4'b0111;
    #50 a = 4'b0111; b = 4'b0101;
    #50 a = 4'b1001; b = 4'b0101;
    #50 a = 4'b1001; b = 4'b1101;
    #50 a = 4'b0000; b = 4'b0000;
  end
endmodule