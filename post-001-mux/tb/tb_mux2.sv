module tb;
  timeunit 1ns;
  timeprecision 1ps;
  logic a, b, sel, y;
  logic expected;

  mux2 dut (.a(a), .b(b), .sel(sel), .y(y));

  initial begin
    $dumpfile("mux2.vcd");
    $dumpvars(0, tb);
    for (int i = 0; i < 8; i++) begin
      {a, b, sel} = i[2:0];
      expected = (~sel & a) | (sel & b);
      #1ns;
      if (y !== expected)
        $fatal(1, "a=%b b=%b sel=%b y=%b expected=%b",
               a, b, sel, y, expected);
    end
    $display("PASS: all 8 binary combinations");
    $finish;
  end
endmodule
