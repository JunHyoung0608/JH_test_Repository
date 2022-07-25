module testbench();
  reg d;
  reg clk;
  wire q; 
  wire qb;

  D_latch ag(q, qb, clk, d);

  initial begin
    d = 1'b1; clk = 1'b0;
    #50 d = 1'b0;
    #50 d = 1'b1;
    #50 d = 1'b0; clk = 1'b1;
    #50 d = 1'b1;
    #50 d = 1'b0;
    #50 d = 1'b1; clk = 1'b0;
    #50 d = 1'b0;
    #50 d = 1'b1;
    #50 d = 1'b1; clk = 1'b1;
    #50 d = 1'b0;
    #50 d = 1'b1;
    #50 d = 1'b0; clk = 1'b0;
  end
endmodule
