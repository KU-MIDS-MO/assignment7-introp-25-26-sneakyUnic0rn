[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/S4wQm4j4)
## Introduction to Programming
## Winter Semester 2025/26 — Assignment 7

All concepts required for these tasks have been covered in the lectures and examples.

---

## Task 1 —Safe function call

Write a function:

safe_call(func, a, b)

that attempts to call the function func with the given arguments.

The function must return a tuple of three elements:

- a boolean indicating whether the call was successful,

- the result of the function call (or None if an error occurred),

- the name of the exception as a string (or None if no error occurred).

If the function call raises one of the following exceptions:

- ZeroDivisionError

- TypeError

- ValueError

- IndexError

- KeyError

the function must not crash, but instead return information about the error.

Any other exception types should not be handled.
---

## Task 2 —Bank acount with nested functions

Write a function:

make_account(initial_balance)


that creates and returns two functions representing operations on a bank account:

- a function for depositing money,

- a function for withdrawing money.

The account balance must be initialized using initial_balance and must persist betwen function calls.

The following rules apply;

- Deposits and withdrawals must use positive numeric values.

- The account balance must never become negative.

- Invalid operations must raise appropriate Python exceptions.

- The account balance must not be directly accessible from outside the returned functions.
---

## Task 3 — Operation pipeline

Write a function:

build_pipeline(operation_names)


where operation_names is a list of strings.

The function must return a new function that applies a sequence of operations to a single input value,in the given order.

Each string in operation_names represents an operation



If an unknown operation name is encountered, an error must be raised.

Calling the returned function should apply all operations sequentially and return the final result.


