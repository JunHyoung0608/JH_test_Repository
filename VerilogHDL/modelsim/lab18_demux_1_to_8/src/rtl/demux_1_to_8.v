module demux_1_to_8(out,s);
 
  input [2:0]s;
  output reg [7:0]out;

  always @(s)

  case(s)
    3'b000:out = 8'b1000_0000;
    3'b001:out = 8'b0100_0000;
    3'b010:out = 8'b0010_0000;
    3'b011:out = 8'b0001_0000;
    3'b100:out = 8'b0000_1000;
    3'b101:out = 8'b0000_0100;
    3'b110:out = 8'b0000_0010;
    3'b111:out = 8'b0000_0001;
    default:out = 8'b0000_0000;
  endcase
endmodule