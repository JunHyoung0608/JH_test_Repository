module testbench();
  reg d;
  reg clk;
  wire q; 
  wire qb;

  d_ff ag(q, qb, clk, d);

  initial begin
    clk = 1'b0; d = 1'b0;
    #50 clk = 1'b1; 
    #50 clk = 1'b0;
    #50 clk = 1'b1;
    #50 clk = 1'b0; d = 1'b1;
    #50 clk = 1'b1;  
    #50 clk = 1'b0;
    #50 clk = 1'b1;
  end
endmodule