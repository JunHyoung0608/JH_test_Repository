module ring_counter(q, clk, reset);
  input clk, reset;
  output reg [2:0]q;

  always @(posedge clk) begin
    if(reset) begin
      q = 3'b100;
    end
    else begin
      case(q)
        3'b100 : q = 3'b110;
        3'b110 : q = 3'b011;
        3'b011 : q = 3'b001;
        3'b001 : q = 3'b100;
      endcase
    end
  end
endmodule