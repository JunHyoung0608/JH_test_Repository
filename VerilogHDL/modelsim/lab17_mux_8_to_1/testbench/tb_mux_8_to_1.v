module testbench();
 
  reg [7:0]s;
  wire [7:0]out;

  mux_8_to_1 ag(out, s);

  initial begin
   s = 3'b000;
   #50 s = 3'b001;
   #50 s = 3'b010;
   #50 s = 3'b011;
   #50 s = 3'b100;
   #50 s = 3'b101;
   #50 s = 3'b110;
   #50 s = 3'b111;
   #50 s = 3'b000;
  end
endmodule