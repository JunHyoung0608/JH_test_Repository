module testbench();
    reg = i0, i1, i2, i3;
    reg = s0, s1;
    wire = out;

    mux4_to_1 ag(i0, i1, i2, i3, s0, s1, out);

    initial begin
        i0 = 2'b00; i1 = 2'b01; i2 = 2'b10; i3 = 2'b11; s0 = 1'b0; s1 = 1'b0;
