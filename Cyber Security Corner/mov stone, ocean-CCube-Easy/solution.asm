section .data
    num1 dw 48   ; Define the first integer (word-sized)
    num2 dw 120  ; Define the second integer (word-sized)
    result dw 0  ; Define a variable to store the result (word-sized), initially set to 0

section .text
    global _start
_start:
    mov ax, word [num1]     ; Move the value of "num1" into the AX register
    mul word [num2]         ; Multiply the value in AX with the value of "num2"
    mov word [result], ax   ; Move the result from AX into the "result" variable