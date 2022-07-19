module testbench();

  reg [2:0]in;
  wire [7:0]y;

  decoder_3_to_8 ag(y, in);

  initial begin
    in = 3'b000; 
    #50 in = 3'b001;
    #50 in = 3'b010;
    #50 in = 3'b011;
    #50 in = 3'b100;
    #50 in = 3'b101;
    #50 in = 3'b110;
    #50 in = 3'b111;
    #50 in = 3'b000;
  end
endmodule
