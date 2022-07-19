module comparator(out, a, b);
  input [1:0]a;
  input [1:0]b;
  output out;

  assign out = (a == b) ? 1'b1 : 1'b0;
endmodule