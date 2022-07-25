module testbench();
  reg t;
  reg clk;
  reg reset;
  wire q; 
  wire qb;

  t_ff ag(q, qb, clk, reset, t);

  initial begin
    t = 1'b0; reset = 1'b0; clk = 1'b0;
    #50 reset = 1'b1;
    #50 reset = 1'b0;
    #100 t = 1'b1;
    #200 $stop;
  end

  always #50 clk = ~clk;
endmodule