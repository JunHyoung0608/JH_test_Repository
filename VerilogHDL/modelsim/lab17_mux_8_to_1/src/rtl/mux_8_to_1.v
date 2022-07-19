module mux_8_to_1(out, s);

  input [2:0]s;
  output reg [7:0]out;

  always @(*)
  case(s)
    3'b000:out = 3'd0;
    3'b001:out = 3'd1;
    3'b010:out = 3'd2;
    3'b011:out = 3'd3;
    3'b100:out = 3'd4;
    3'b101:out = 3'd5;
    3'b110:out = 3'd6;
    3'b111:out = 3'd7;
  endcase

endmodule