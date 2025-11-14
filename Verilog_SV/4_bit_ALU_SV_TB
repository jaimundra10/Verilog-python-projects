************************************************SYSTEM VERILOG TESTBENCH*********************************
class first;
  rand bit [3:0] a, b;
  rand bit [2:0] co;
  bit [4:0] expected;

  // Display method
  function void display(logic [4:0] result);
    $display("value of a: %0d, value of b: %0d, co: %0d, expected: %0d, result: %0d", a, b, co, expected, result);
  endfunction

  // Compute expected result
  function void compute_expected();
    case (co)
      3'b000: expected = a + b;
      3'b001: expected = a - b;
      3'b010: expected = a & b;
      3'b011: expected = a | b;
      3'b100: expected = a ^ b;
      3'b101: expected = ~a;
      3'b110: expected = a + 1;
      3'b111: expected = a - 1;
      default: expected = 0;
    endcase
  endfunction
endclass

module alu_tb;

  logic [3:0] a, b;
  logic [2:0] co;
  logic [4:0] result;

  first f;

  alu dut (
    .a(a),
    .b(b),
    .co(co),
    .result(result)
  );

  // Task to run one transaction
  task automatic run_txn(ref first f);
    a = f.a;
    b = f.b;
    co = f.co;
    #10;
    f.compute_expected();
    f.display(result);
    assert(result == f.expected) else $error("❌ Mismatch detected!");
  endtask

  // Initial block to run test
  initial begin
    f = new();
    for (int i = 0; i < 20; i++) begin
      assert(f.randomize());
      run_txn(f);
    end
    $finish;
  end

endmodule
