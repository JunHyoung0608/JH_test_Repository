module testbench();
    reg i0, i1, i2, i3, i4, i5, i6, i7;
    wire out0, out1, out2;

    encoder_8_to_3 ag(out0, out1, out2, i0, i1, i2, i3, i4, i5, i6, i7);

    initial begin
        i0 = 1'b1; i1 = 1'b0; i2 = 1'b0; i3 = 1'b0; i4 = 1'b0; i5 = 1'b0; i6 = 1'b0; i7 = 1'b0;
        #50 i0 = 1'b0; i1 = 1'b1;
        #50 i1 = 1'b0; i2 = 1'b1;
        #50 i2 = 1'b0; i3 = 1'b1;
        #50 i3 = 1'b0; i4 = 1'b1;
        #50 i4 = 1'b0; i5 = 1'b1;
        #50 i5 = 1'b0; i6 = 1'b1;
        #50 i6 = 1'b0; i7 = 1'b1;
        #50 i7 = 1'b0;
    end
endmodule

