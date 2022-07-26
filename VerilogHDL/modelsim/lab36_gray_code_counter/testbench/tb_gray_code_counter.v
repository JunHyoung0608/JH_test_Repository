module testbench();
  reg clk, reset;
  wire [2:0]q;

  gray_code_counter ag(q, clk, reset);

  initial begin
    clk = 1'b0; reset = 1'b1;
    #100 reset = 1'b0;
    #1000 $stop;
  end

  always #50 clk = ~clk;
endmodule