module D_latch(q, qb, clk, d);
  input d, clk;
  output reg q, qb;

  always @(clk) begin
    if(clk == 1'b1) begin
      q = d; qb = ~d;
    end
  end
endmodule