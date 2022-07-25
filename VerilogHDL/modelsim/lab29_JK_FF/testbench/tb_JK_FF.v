module testbench();
  reg j, k;
  reg clk;
  wire q; 
  wire qb;

  jk_ff ag(q, qb, clk, j, k);

  initial begin
    clk = 1'b0; j = 1'b0; k = 1'b0;
    #50 clk = 1'b0; 
    #50 clk = 1'b1; k = 1'b1;
    #50 clk = 1'b0;
    #50 clk = 1'b1; j = 1'b1; k = 1'b0;
    #50 clk = 1'b0;  
    #50 clk = 1'b1; k = 1'b1;
    #50 clk = 1'b0;
  end
endmodule
