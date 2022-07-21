module half_subtractor(bor, diff, x, y);
  input x, y;
  output reg bor, diff;

  assign bor = ~x && y;
  assign diff = x ^ y;
endmodule