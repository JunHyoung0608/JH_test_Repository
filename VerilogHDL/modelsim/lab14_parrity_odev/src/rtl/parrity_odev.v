module parrity_odev(out_odd, out_even, i0, i1, i2);
    input i0, i1, i2;
    output out_odd;
    output out_even;
    
    wire i0n, i1n, i2n;
    wire a0, a1, a2, a3, a4, a5, a6, a7;

    not(i0n, i0);
    not(i1n, i1);
    not(i2n, i2);

    and(a0, i0n, i1n, i2n);
    and(a1, i0n, i1, i2);
    and(a2, i0, i1n, i2);
    and(a3, i0, i1, i2n);
    and(a4, i0n, i1n, i2);
    and(a5, i0n, i1, i2n);
    and(a6, i0, i1n, i2n);
    and(a7, i0, i1, i2);

    or(out_odd, a0, a1, a2, a3);
    or(out_even, a4, a5, a6, a7);
endmodule