module add_sub_4bit(cd ,value, w, a, b);
  input w;
  input [3:0]a;
  input [3:0]b;
  output cd;
  output [3:0]value;

  if w == 0 begin
    assign {cd, value} = a + b;
  end
  else begin
    if w == 1 begin
      //감산기
    end
  end