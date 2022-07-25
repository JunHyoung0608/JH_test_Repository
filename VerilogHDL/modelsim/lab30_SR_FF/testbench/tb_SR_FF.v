module testbench();
  reg s, r;
  reg clk;
  wire q; 
  wire qb;

  sr_ff ag(q, qb, clk, s, r);

  initial begin
    clk = 1'b0; s = 1'b0; r = 1'b0;
    #50 clk = 1'b1; 
    #50 clk = 1'b0; r = 1'b1;
    #50 clk = 1'b1;
    #50 clk = 1'b0; s = 1'b1; r = 1'b0;
    #50 clk = 1'b1;  
    #50 clk = 1'b0; r = 1'b1;
    #50 clk = 1'b1;
  end
endmodule
