module testbench();
  reg x, y, b;
  wire borrow, difference;

  full_subtractor ag(borrow, difference, x, y, b);

  initial begin
    x = 1'b0; y = 1'b0; b = 1'b0;
    #50 x = 1'b0; y = 1'b0; b = 1'b1;
    #50 x = 1'b0; y = 1'b1; b = 1'b0;
    #50 x = 1'b0; y = 1'b1; b = 1'b1;
    #50 x = 1'b1; y = 1'b0; b = 1'b0;
    #50 x = 1'b1; y = 1'b0; b = 1'b1;
    #50 x = 1'b1; y = 1'b1; b = 1'b0;
    #50 x = 1'b1; y = 1'b1; b = 1'b1;
  end
endmodule
