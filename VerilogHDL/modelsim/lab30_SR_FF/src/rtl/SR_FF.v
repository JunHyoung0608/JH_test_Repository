module sr_ff(q, qb, clk, s, r);
  input s, r, clk;
  output reg q, qb;

  always @(clk) begin
    if(clk == 1'b1) begin
      if(s == 1'b0 && r == 1'b1) begin
        q = 1'b0; qb = 1'b1;
      end
      else if(s == 1'b1 && r == 1'b0) begin
        q = 1'b1; qb = 1'b0;
      end
      else if(s == 1'b1 && r == 1'b1) begin
        q = ~q; qb = ~qb;
      end
    end
  end
endmodule