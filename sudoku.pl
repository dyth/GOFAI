:- use_module(library(bounds)).

diff(L) :- L in 1..9, all_different(L).

rows([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P]) :- diff([A, B, C, D]), diff([E, F, G, H]), diff([I, J, K, L]), diff([M, N, O, P]).
cols([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P]) :- diff([A, E, I, M]), diff([B, F, J, N]), diff([C, G, K, O]), diff([D, H, L, P]).
box([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P]) :- diff([A, B, E, F]), diff([C, D, G, H]), diff([I, J, M, N]), diff([K, L, O, P]).

sudoku(L) :- rows(L), cols(L), box(L), label(L).
