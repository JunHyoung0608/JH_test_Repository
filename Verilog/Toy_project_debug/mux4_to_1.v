module mux4_to_1(i0, i1, i2, i3, s0, s1, out);
    output out;
    input i0, i1, i2, i3
    input s0, s1;

    wire s1n, s0n;
    wire y0, y1, y2, y3;

    not(s0n, s0);
    not(s1n, s1);

    and(y0, i0, s0n, s1n);
    and(y1, i1, s0, s1n);
    and(y2, i2, s1, s0n);
    and(y3, i3, s0, s1);

    or(y0, y1, y2, y3, out);
endmodule