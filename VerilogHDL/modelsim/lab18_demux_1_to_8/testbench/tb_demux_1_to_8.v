module testbench();
  reg [2:0]s;
  wire [7:0]out;

  demux_1_to_8 ag(out, s);

  initial begin
    s = 3'b000;
    #50 s = 3'b001;
    #50 s = 3'b010;
    #50 s = 3'b011;
    #50 s = 3'b100;
    #50 s = 3'b101;
    #50 s = 3'b110;
    #50 s = 3'b111;
  end
endmodule