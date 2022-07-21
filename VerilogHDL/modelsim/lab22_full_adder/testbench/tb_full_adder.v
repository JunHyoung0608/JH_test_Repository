module testbench();
  reg [2:0]x;
  wire carry, sum;

  full_adder ag(carry, sum, x);

  initial begin
    x = 3'b000;
    #50 x = 3'b001;
    #50 x = 3'b010;
    #50 x = 3'b011;
    #50 x = 3'b100;
    #50 x = 3'b101;
    #50 x = 3'b110;
    #50 x = 3'b111;
  end
endmodule