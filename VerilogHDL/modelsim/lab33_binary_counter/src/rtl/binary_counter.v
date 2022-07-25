module binary_counter(q, clk, reset, x);
  input x, clk, reset;
  output reg [2:0]q;

  always @(posedge clk) begin
    if(reset) begin
      q = 3'b0;
    end
    else begin
      if(x == 1'b0) begin
        if(q == 3'b111) begin
          q = 4'b0;
        end
        else begin
          q = q + 4'b1;
        end
      end
      else if(x == 1'b1) begin
        if (q == 3'b0) begin
          q = 3'b111;
        end
        else begin
          q = q - 3'b001;
        end
      end
    end
  end
endmodule
