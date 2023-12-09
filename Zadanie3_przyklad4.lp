%Tabela z danymi


person(Miroslaw, 75, 25, 202, 130, 165).
person(Jacek, 87, 24, 198, 127, 173).
person(Piotr, 68, 19, 195, 121, 164).
person(Szymon, 91, 20, 207, 122, 182).
person(Pawel, 80, 28, 215, 125, 172).
person(Tomasz, 78, 22, 197, 125, 180).
person(Mateusz, 75, 25, 205, 127, 178).
person(Lukasz, 81, 23, 211, 131, 165).


find_and_display_max(List) :-
    max_list(List, Max),
    write("Maksymalna wartosc z listy: "), write(Max), nl.

kandydat(X1, X2, X3, X4, X5, X6, X7, X8).
daneSzermierka(75, 87, 68, 91, 80, 78, 75, 81).
danePlywanie(25, 24, 19, 20, 28, 22, 25, 23).
daneJezdziectwo(202, 198, 195, 207, 215, 197, 205, 211).
daneBieg(130, 127, 121, 122, 125, 125, 127, 131).
daneStrzelanie(165, 173, 164, 182, 172, 180, 178, 165).


daneSzermierka(Szermierka), find_and_display_max(Szermierka).
________________________________________________________________________________

% Dane wejściowe - informacje o osobach
person(miroslaw, 75, 25, 202, 130, 165).
person(jacek, 87, 24, 198, 127, 173).
person(piotr, 68, 19, 195, 121, 164).
person(szymon, 91, 20, 207, 122, 182).
person(pawel, 80, 28, 215, 125, 172).
person(tomasz, 78, 22, 197, 125, 180).
person(mateusz, 75, 25, 205, 127, 178).
person(lukasz, 81, 23, 211, 131, 165).

% Znajdź maksymalną wartość dla każdej kategorii
max_value_per_category(MaxSzermierka, MaxPlywanie, MaxJezdziectwo, MaxBieg, MaxStrzelanie) :-
    MaxSzermierka = #max { S : person(_, S, _, _, _, _) },
    MaxPlywanie = #max { P : person(_, _, P, _, _, _) },
    MaxJezdziectwo = #max { J : person(_, _, _, J, _, _) },
    MaxBieg = #max { B : person(_, _, _, _, B, _) },
    MaxStrzelanie = #max { T : person(_, _, _, _, _, T) }.

% Ograniczenie, aby wybrać tylko jedną wartość dla każdej kategorii
:- not #count { X : max_value_per_category(_, _, _, _, X) } = 1.

% Dodaj fakty, aby przechować wartości MaxSzermierka
max_szermierka(MaxSzermierka) :- max_value_per_category(MaxSzermierka, _, _, _, _).
max_plywanie(MaxPlywanie) :- max_value_per_category(_, MaxPlywanie, _, _, _).
max_jezdziectwo(MaxJezdziectwo) :- max_value_per_category(_, _, MaxJezdziectwo, _, _).
max_bieg(MaxBieg) :- max_value_per_category(_, _, _, MaxBieg, _).
max_strzelanie(MaxStrzelanie) :- max_value_per_category(_, _, _, _, MaxStrzelanie).

% Suma wartości
sum_of_max_values(Sum) :-
    Sum = MaxSzermierka + MaxPlywanie + MaxJezdziectwo + MaxBieg + MaxStrzelanie,
    max_szermierka(MaxSzermierka), max_plywanie(MaxPlywanie),
    max_jezdziectwo(MaxJezdziectwo), max_bieg(MaxBieg),
    max_strzelanie(MaxStrzelanie).

% Osoba z najwyższym wynikiem w danej kategorii
person_with_max_value(S, P, J, B, T) :-
    person(S, Szermierka, _, _, _, _),
    Szermierka = MaxSzermierka,
    max_szermierka(MaxSzermierka),
    
    person(P, _, Plywanie, _, _, _),
    Plywanie = MaxPlywanie,
    max_plywanie(MaxPlywanie),
    
    person(J, _, _, Jezdziectwo, _, _),
    Jezdziectwo = MaxJezdziectwo,
    max_jezdziectwo(MaxJezdziectwo),
    
    person(B, _, _, _, Bieg, _),
    Bieg = MaxBieg,
    max_bieg(MaxBieg),
    
    person(T, _, _, _, _, Strzelanie),
    Strzelanie = MaxStrzelanie,
    max_strzelanie(MaxStrzelanie).

% Wyświetl wyniki
#show max_value_per_category/5.
#show max_szermierka/1.
#show max_plywanie/1.
#show max_jezdziectwo/1.
#show max_bieg/1.
#show max_strzelanie/1.
#show sum_of_max_values/1.
#show person_with_max_value/5.





_________________________________
DOBRY POMYSŁ

% Dane wejściowe - informacje o osobach
person(miroslaw, 75, 25, 202, 130, 165).
person(jacek, 87, 24, 198, 127, 173).
person(piotr, 68, 19, 195, 121, 164).
person(szymon, 91, 20, 207, 122, 182).
person(pawel, 80, 28, 215, 125, 172).
person(tomasz, 78, 22, 197, 125, 180).
person(mateusz, 75, 25, 205, 127, 178).
person(lukasz, 81, 23, 211, 131, 165).

% Definicja sumy punktów
sum_of_values(Sum) :-
    Sum = #sum { V : person(_, V, _, _, _, _) }.

% Zbiór par (osoba, wynik)
{ score(Name, Value) : person(Name, Value, _, _, _, _) }.

% Osoby nie mogą się powtarzać
:- score(Name1, Value), score(Name2, Value), Name1 != Name2.

% Minimalizuj liczbę osób w wyniku
#minimize{ 1 : score(_, _) }.

% Wyświetl wyniki
#show sum_of_values/1.
#show score/2.
















________________________________________________________________________________
%TO CO DZIAŁA DO TEJ PORY
% Dane wejściowe - informacje o osobach
person(miroslaw, 75, 25, 202).
person(jacek, 87, 24, 198).
person(piotr, 68, 19, 195).
person(szymon, 91, 20, 207).

% Znajdź maksymalną wartość dla każdej kategorii
max_value_per_category(MaxSzermierka, MaxPlywanie, MaxJezdziectwo) :-
    MaxSzermierka = #max { S : person(_, S, _, _) },
    MaxPlywanie = #max { P : person(_, _, P, _) },
    MaxJezdziectwo = #max { J : person(_, _, _, J) }.

% Ograniczenie, aby wybrać tylko jedną wartość dla każdej kategorii
:- not max_value_per_category(_, _, _).

% Wyświetl wyniki
#show max_value_per_category/3.




