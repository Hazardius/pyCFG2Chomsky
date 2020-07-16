# pyCFG2Chomsky

System transforming Context Free Grammar(CFG) into Chomsky normal form.

---

## Input data format

Each rule from CFG should be in correct form:

    NONTERM -> [ε,TERM,NONTERM]*

where NONTERM is typed as a string with length bigger then 1 char, and TERM is any char except ε.

---

## Output

For any correct CFG project should print out all rules from CFG in a Chomsky normal form.

---

## Usage

To run project write a CFG down in a file (for example - check [test_data.txt](test_data.txt)) and use command:

    cat test_data.txt | python __init__.py
