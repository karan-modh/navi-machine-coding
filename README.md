# navi-machine-coding-interview

The following repository contains the submission for my Navi Machine coding interview which consisted of designing a Loan Disbursement and Payment checking system.

The input would be of three types : `LOAN`, `PAYMENT`, `BALANCE`.

- When the input is of `LOAN` type, A new loan needs to be created and EMI amount and number of EMIs needs to be calculated.
- When the input is of `PAYMENT` type, A lumpsum payment is made for some loan and hence the new number of emis needs to be calculated (EMI amount remains the same).
- When the input is of `BALANCE` type, The output should be shown which consists of amount paid till date and the number of EMIs left.

### Steps to run:
- `python3 main.py <filename/filepath>`

### Input Format:
- `LOAN BANK_NAME BORROWER_NAME PRINCIPAL NO_OF_YEARS RATE_OF_INTEREST`
- `PAYMENT BANK_NAME BORROWER_NAME LUMP_SUM_AMOUNT EMI_NO`
- `BALANCE BANK_NAME BORROWER_NAME EMI_NO`

### Output Format (To be shown only on the BALANCE input):
- `BANK_NAME BORROWER_NAME AMOUNT_PAID NO_OF_EMIS_LEFT`
