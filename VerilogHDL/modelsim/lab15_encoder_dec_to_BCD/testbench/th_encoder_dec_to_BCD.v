module testbench();
    reg      i0, i1, i2, i3, i4, i5, i6, i7, i8, i9;
    wire [3:0]out;

    encoder_dec_to_BCD ag(out, i0, i1, i2, i3, i4, i5, i6, i7, i8, i9);

    initial begin
        i0 = 1'b1; i1 = 1'b0; i2 = 1'b0; i3 = 1'b0; i4 = 1'b0; i5 = 1'b0; i6 = 1'b0; i7 = 1'b0; i8 = 1'b0; i9 = 1'b0;
        #20 i0 = 1'b0; i1 = 1'b1;
        #20 i1 = 1'b0; i2 = 1'b1;
        #20 i2 = 1'b0; i3 = 1'b1;
        #20 i3 = 1'b0; i4 = 1'b1;
        #20 i4 = 1'b0; i5 = 1'b1;
        #20 i5 = 1'b0; i6 = 1'b1;
        #20 i6 = 1'b0; i7 = 1'b1;
        #20 i7 = 1'b0; i8 = 1'b1;
        #20 i8 = 1'b0; i9 = 1'b1;
        #20 i9 = 1'b0;
    end
endmodule