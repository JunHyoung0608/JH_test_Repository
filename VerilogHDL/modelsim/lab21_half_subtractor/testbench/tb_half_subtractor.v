module testbench();
  reg x, y;
  wire bor, diff;

  half_subtractor ag(bor, diff, x, y);

  initial begin
    x = 1'b0; y = 1'b0;
    #50 x = 1'b0; y  = 1'b1;
    #50 x = 1'b1; y  = 1'b0;
    #50 x = 1'b1; y  = 1'b1;
    #50 x = 1'b0; y = 1'b0;

  end
endmodule