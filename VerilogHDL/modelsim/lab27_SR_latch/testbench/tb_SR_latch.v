module testbench();
  reg s, r;
  wire q; 
  wire qb;

  SR_latch ag(q, qb, s, r);

  initial begin
    s = 1'b0; r = 1'b0;
    #50 s = 1'b0; r = 1'b1;
    #50 s = 1'b1; r = 1'b0;
    #50 s = 1'b1; r = 1'b1;
    #50 s = 1'b0; r = 1'b0;
  end
endmodule
