module testbench();
  reg x;
  reg reset;
  reg clk;
  wire [2:0]q;

  binary_counter ag(q, clk, reset, x);


  initial begin
    x = 1'b0; clk = 0; reset = 1'b1;
    #100 reset = 1'b0;
    #800 x = 1'b1;
    #800 $stop;
  end

  always #50 clk  =~clk;
endmodule