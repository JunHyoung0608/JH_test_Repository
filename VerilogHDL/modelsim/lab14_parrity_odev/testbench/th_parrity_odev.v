module testbench();
    reg i0, i1, i2;
    wire out_even, out_odd;

    parrity_odev ag(out_odd, out_even, i0, i1, i2);

    initial begin
        i0 = 1'b0; i1 = 1'b0; i2 = 1'b0;
        #20; i0 = 1'b0; i1 = 1'b0; i2 = 1'b1;
        #20; i0 = 1'b0; i1 = 1'b1; i2 = 1'b0;
        #20; i0 = 1'b0; i1 = 1'b1; i2 = 1'b1;
        #20; i0 = 1'b1; i1 = 1'b0; i2 = 1'b0;
        #20; i0 = 1'b1; i1 = 1'b0; i2 = 1'b1;
        #20; i0 = 1'b1; i1 = 1'b1; i2 = 1'b0;
        #20; i0 = 1'b1; i1 = 1'b1; i2 = 1'b1;
    end
endmodule