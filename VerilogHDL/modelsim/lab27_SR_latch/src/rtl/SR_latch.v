module SR_latch(q, qb, s, r);
  input s, r;
  output reg q, qb;

always @(*)
case({s, r})
  2'b01 : begin q = 1'b0; qb = 1'b1;end
  2'b10 : begin q = 1'b1; qb = 1'b0;end
  2'b11 : begin q = 1'b0; qb = 1'b0;end
endcase
endmodule 