module t_ff(q, qb, clk, reset,t);
  input t, clk, reset;
  output reg q, qb;

  always @(posedge clk) begin
    if(clk == 1'b1) begin
      if(reset) begin
        q = 1'b0; qb = 1'b1;
      end
      else if(t) begin
        q = ~q; qb = ~qb;
      end
    end
  end
endmodule