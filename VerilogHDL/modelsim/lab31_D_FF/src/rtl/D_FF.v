module d_ff(q, qb, clk, d);
  input d, clk;
  output reg q, qb;

  always @(clk) begin
    if(clk == 1'b1) begin
      if(d == 0) begin
        q = 1'b0; qb = 1'b1;
      end
      else if(d == 1) begin
        q = 1'b1; qb = 1'b0;
      end
    end
  end
endmodule