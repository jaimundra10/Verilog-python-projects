ALU Testbench Project//////////////////////////////////////////////////////////////////////
This project implements a SystemVerilog testbench for a simple Arithmetic Logic Unit (ALU) supporting basic operations like addition, subtraction, bitwise logic, and unary operations.

Randomized testing using a class-based transaction object

Self-checking testbench with expected output computation

Assertion-based validation to catch mismatches

Modular structure separating DUT and test logic

Looped execution for multiple test cases

🧪 Testbench Components Used
class first: Encapsulates randomized inputs (a, b, co) and expected output logic

compute_expected(): Function to calculate expected ALU result based on opcode

display(): Method to print input, expected, and actual result

run_txn(ref f): Task to drive DUT inputs, wait for result, and validate correctness

initial block: Runs 20 randomized test iterations using a for loop
//////////////////////////////////////////////////////////////////////

*************************************************DESIGN CODE OF ALU**********************************************
module alu (
    input  logic [3:0] a,
    input  logic [3:0] b,
    input  logic [2:0] co,
    output logic [4:0] result
);

always_comb begin
    case (co)
        3'b000: result = a + b;
        3'b001: result = a - b;
        3'b010: result = a & b;
        3'b011: result = a | b;
        3'b100: result = a ^ b;
        3'b101: result = ~a;
        3'b110: result = a + 1;
        3'b111: result = a - 1;
        default: result = 0;
    endcase
end

endmodule

