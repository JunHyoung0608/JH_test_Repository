module full_adder(carry, sum, x);
  input [2:0]x;
  output carry;
  output sum;

  assign {carry, sum} = x[2] + x[1] + x[0];
endmodule