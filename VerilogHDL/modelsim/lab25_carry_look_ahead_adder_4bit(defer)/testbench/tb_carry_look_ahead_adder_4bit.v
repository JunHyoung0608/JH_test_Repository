module testbench();
  reg [3:0]a;
  reg [3:0]b;
  wire carry;

  carry_look_ahead_adder_4bit ag(carry, a, b);

  integer i, j;

  initial begin
    a = 4'b0000; b = 4'b0000;
    for (i = 0; i <= 16; i = i + 1)
      for (j = 0; j <= 16; j = j + 1) begin
        #50 a = a + 4'b0001; b = b + 4'b0001;
  end
endmodule