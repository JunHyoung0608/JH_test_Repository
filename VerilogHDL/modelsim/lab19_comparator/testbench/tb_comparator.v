module testbench();
  reg [1:0]a;
  reg [1:0]b;
  wire out;

  comparator ag(out, a, b);

  initial begin
    a = 2'b00; b = 2'b00;
    #50 a = 2'b01;
    #50 a = 2'b10;
    #50 a = 2'b11;
    #50 a = 2'b00; b = 2'b01;
    #50 a = 2'b01;
    #50 a = 2'b10;
    #50 a = 2'b11;
    #50 a = 2'b00; b = 2'b10;
    #50 a = 2'b01;
    #50 a = 2'b10;
    #50 a = 2'b11;
    #50 a = 2'b00; b = 2'b11;
    #50 a = 2'b01;
    #50 a = 2'b10;
    #50 a = 2'b11;
    #50 a = 2'b00;
  end
endmodule