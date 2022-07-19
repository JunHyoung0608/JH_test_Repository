module encoder_dec_to_BCD(out, i0, i1, i2, i3, i4, i5, i6, i7, i8, i9);
    input i0, i1, i2, i3, i4, i5, i6, i7, i8, i9;
    output [3:0]out;

    or(a, i8, i9);
    or(b, i4, i5, i6, i7);
    or(c, i2, i3, i6, i7);
    or(d0, i1, i3, i5, i7);
    or(d1, d0, i9);
    assign out = {a, b, c, d1};
endmodule
