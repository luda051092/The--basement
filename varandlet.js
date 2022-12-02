ES5 global constants:
var PI = 3.14;
PI = 42; // stop me from doing this!

ES2015 Global Constants:

const PI = 3.14;
PI = 42; // Error!

Difference between Var and Let:
Var can reassign and redeclare, but let cannot. Var can access hoisted variables. Let creates block scope, which means that
access is restricted from outside the block. 

Difference between var and const:
Can reassign and redeclare with var; can access hoisted variable with var but not const. Const also creates block scope. 

What is hoisting? 
Hoisting is when in JS a variable is "hoisted", or lifted to the top of the scope in which they are declared. In var, we can 
access the name of the variable before it is used.
Function declarations are also hoisted. They can be invoked before being defined in a database. 
