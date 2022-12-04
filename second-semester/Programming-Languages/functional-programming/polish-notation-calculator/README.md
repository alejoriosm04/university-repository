 <h1 align = "center">Polish Notation Calculator in Haskell</h1>

An implementation of a polish notation (PN)[^definition] calculator in Haskell using the functional programming paradigm.

Project for the second-semester course "Programming Languages" (ST0244) taught at EAFIT University (Medellín, Colombia) by prof Edison Valencia.

## Features

- 📥 Checks valid syntax of polish notation (PN) expressions

- 🔁 Calculate endlessly (no need to execute the program each time)

## Motivation

The main aim of this project was to use the concepts of the functional paradigm in the analysis of polish notation in Haskell and data collection management in Haskell.

## Method

###  Flow

1. The user inputs a polish notation (PN) expression.

2. Prompts the user the result

3. Finally, the user can input a new PN expression.

### Technical details

- Makes use of the **stack** memory model for the operations related to the linked lists. Where the last item in a linked list, is the first out of it (LIFO).

- Use of data collection management

- Modeled towards functional programming.

## Documentation

**Note:** Please read the instructions and suggestions displayed at the start.

- **Evaluate and calculate** PN expressions:

    > 4 -72.4 8 * +

    > 2 3 * 6 + 8 /

- **Operators**: addition (`+`), subtraction (`-`), multiplication
    (`*`), division (`/`), power (`^`), natural logarithm (`ln`) and sum (`sum`).

- **Decimal numbers** (dot as decimal separator) and **negative numbers**.

### Caveats

PN expressions have a certain way to be declared algebraically. Please be sure of the syntax to avoid errors in execution.

The program breaks if the input is invalid.

## Install

- Binaries are in pre-release.

- Clone the repo:

        git clone https://github.com/alejoriosm04/university-repository/tree/main/Programming-Languages/functional-programming/polish-notation-calculator

## Related projects

-  [linasofi13/practica2_lenguajesProg ](https://github.com/linasofi13/practica2_lenguajesProg) (2022) [Haskell]
- [alejoriosm/polish-notation-calculator](https://github.com/alejoriosm04/polish-notation-calculator) (2022) [C++]

## Contribute

You are welcome to submit issues or pull requests.

## Authors

The design of the program was taken as a reference from [Learn Haskell for the good of all](http://aprendehaskell.es/main.html).

[Alejandro Ríos](https://github.com/alejoriosm04) developed the entire program.

## License

Copyright 2022 Alejandro Ríos.

[^definition]: [Wikipedia](https://en.wikipedia.org/wiki/Polish_notation): "A mathematical notation in which operators precede their operands".