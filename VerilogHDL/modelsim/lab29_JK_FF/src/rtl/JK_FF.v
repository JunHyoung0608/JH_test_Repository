module jk_ff(q, qb, clk, j, k);
  input j, k, clk;
  output reg q, qb;

  always @(clk) begin
    if(clk == 1'b1) begin
      if(j == 1'b0 && k == 1'b1) begin
        q = 1'b0; qb = 1'b1;
      end
      else if(j == 1'b1 && k == 1'b0) begin
        q = 1'b1; qb = 1'b0;
      end
      else if(j == 1'b1 && k == 1'b1) begin
        q = ~q; qb = ~qb;
      end
    end
  end
endmodule