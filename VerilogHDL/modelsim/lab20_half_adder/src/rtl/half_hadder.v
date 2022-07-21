module half_hadder(s, c, a, b);
  input a, b;
  output c ,s;

  and(c, a, b);
  xor(s, a, b);
endmodule