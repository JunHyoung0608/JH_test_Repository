module full_subtractor(borrow, difference, x, y, b);
  input x, y, b;
  output borrow, difference;

  assign borrow = (~x && y) || (~(x ^ y) && b);
  assign difference = ~(~(x ^ y) ^ b);
endmodule