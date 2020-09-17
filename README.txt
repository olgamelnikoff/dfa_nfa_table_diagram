The program takes the user’s input as states and alphabet symbols and converts the input into a transition table for a Deterministic Finite Automaton (DFA) or Non-deterministic Finite Automaton (NFA) and a corresponding diagram.

1.	The user is first prompted to indicate if the input he is going to enter is for DFA and NFA.
2.	Then the user is asked to enter the alphabet, the states, indicate which state is initial, as well as which state / states are accepting.
3.	For each state entered by the user, the program creates a row in the table and a node in the diagram.
4.	Then the user fills out the table. For each user’s input, the program fills out the appropriate cell in the table and also creates an appropriate edge in the diagram.
5.	Then the table is output using the texttable module, and the diagram is output using the graphviz module.
