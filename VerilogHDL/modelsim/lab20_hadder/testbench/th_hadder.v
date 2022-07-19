module testbench();
  reg a;
  reg b;
  wire s;
  wire c;

  hadder ag(s, c, a, b);

  initial begin
    a = 1'b0; b = 1'b0;
    #50 a = 1'b0; b = 1'b1;
    #50 a = 1'b1; b = 1'b0;
    #50 a = 1'b1; b = 1'b1;
    #50 a = 1'b0; b = 1'b0;
  end
endmodule