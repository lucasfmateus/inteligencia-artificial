% Verifica se um item pertence a uma lista
pertence_a(X, [X | _]).

pertence_a(X, [_ | Cauda]):-
	pertence_a(X, Cauda).


% Exercicio 1
elem_repetidas([],[]).
elem_repetidas([Cabeca | Cauda],[Cabeca | C2]) :-
	pertence_a(Cabeca, Cauda),
	elem_repetidas(Cauda, C2),
	not(pertence_a(Cabeca, C2)).
elem_repetidas([Cabeca | Cauda], L) :-
	not(pertence_a(Cabeca, Cauda)),
	elem_repetidas(Cauda,L).


% Exercicio 2 - Intercalada

intercalada([],[],[]).
intercalada([],L,L).
intercalada(L,[],L).
intercalada([X|R1], [Y|R2], [X,Y|R3]):-
	intercalada(R1,R2,R3).


% Exercicio 3 - Inserção ordenada

insercao_ord(N,[],[N]).
insercao_ord(N,[X|R],[X|L]):-
	N >= X,
	insercao_ord(N,R,L).
insercao_ord(N,[X|R],[N,X|R]):-
	N =< X.


% Exercicio 4 - Ordenada

ordenada([],[]).
ordenada([C1|Cauda], L):-
	insercao_ord(C1,L, L1),
	ordenada(Cauda,L).
