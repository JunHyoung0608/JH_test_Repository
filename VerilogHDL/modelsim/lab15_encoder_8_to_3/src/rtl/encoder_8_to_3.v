module encoder_8_to_3(out0, out1, out2, i0, i1, i2, i3, i4, i5, i6, i7);
    input i0, i1, i2, i3, i4, i5, i6, i7;
    output out0, out1, out2;

    or(out0, i4, i5, i6, i7);
    or(out1, i2, i3, i6, i7);
    or(out2, i1, i3, i5, i7);
endmodule
