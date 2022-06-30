% =======================================================================================
% Primer sa porodicnim stablom. (iz knjige)
% =======================================================================================

 musko(kron).
 musko(posejdon).
 musko(zevs).
 musko(jasion).
 musko(triton).
 musko(apolon).
 musko(pluton).
 zensko(reja).
 zensko(amfitrita).
 zensko(leto).
 zensko(demetra).
 zensko(artemida).
 roditelj(kron,posejdon).
 roditelj(reja,posejdon).
 roditelj(kron,zevs).
 roditelj(reja,zevs).
 roditelj(kron,demetra).
 roditelj(reja,demetra).
 roditelj(posejdon,triton).
 roditelj(amfitrita,triton).
 roditelj(zevs,apolon).
 roditelj(leto,apolon).
 roditelj(zevs,artemida).
 roditelj(leto,artemida).
 roditelj(jasion,pluton).
 roditelj(demetra,pluton).

 predak(X,Y) :- roditelj(X,Y).
 predak(X,Y) :- roditelj(X,Z), predak(Z,Y).
 majka(X,Y) :- zensko(X), roditelj(X,Y).
 otac(X,Y) :- musko(X), roditelj(X,Y).
 brat(X,Y) :- musko(X), roditelj(Z,X), roditelj(Z,Y), X\==Y.
 sestra(X,Y) :- zensko(X), roditelj(Z,X), roditelj(Z,Y), X\==Y.
 tetka(X,Y) :- sestra(X,Z), roditelj(Z,Y).
 stric(X,Y) :- brat(X,Z), otac(Z,Y).
 ujak(X,Y) :- brat(X,Z), majka(Z,Y).
 bratodstrica(X,Y) :- musko(X), otac(Z,X), stric(Z,Y).
 sestraodstrica(X,Y) :- zensko(X), otac(Z,X), stric(Z,Y).
 bratodujaka(X,Y) :- musko(X), otac(Z,X), ujak(Z,Y).
 sestraodujaka(X,Y) :- zensko(X), otac(Z,X), ujak(Z,Y).
 bratodtetke(X,Y) :- musko(X), majka(Z,X), tetka(Z,Y).
 sestraodtetke(X,Y) :- zensko(X), majka(Z,X), tetka(Z,Y).

% ======================================================================================
% Kradljivci
%
% Ko laze taj krade
% Ko krade i uhvacen je u kradji taj ide u zatvor
% Al Kapone laze
% Al Kapone je uhvacen u kradji
% Laki Luciano laze
% Da li Al kapone ide u zatvor? Da li Laki Luciano ide u zatvor?
% ======================================================================================

krade(X):- laze(X).
zatvor(X):- krade(X), uhvacen(X).
laze(alKapone).
uhvacen(alKapone).
laze(lakiLuciano).
% Fakticki zadatak je da se iskuca ovo i ukuca u konzolu zatvor(alKapone) i zatvor(lakiLuciano)

% ======================================================================================
% Bojenje grafa
% Posmatra se karta i na njoj Srbija i njeni susedi.
% Potrebno je naci bojenje karte tkd svaka susedna zemlja bude obojena najmanjim brojem razl boja.
% ======================================================================================

bojenje(Srb, Cg, Mak, Hrv, Bih, Madj, Bug, Rum, Alb):-
	sused(Srb, Cg), sused(Srb, Mak), sused(Srb, Hrv), sused(Srb, Bih), sused(Srb, Madj),
	sused(Srb, Bug), sused(Srb, Rum), sused(Srb, Alb), sused(Cg, Bih), sused(Cg, Bih),
	sused(Cg , Alb), sused(Alb, Mak), sused(Mak, Bug), sused(Bug, Rum), sused(Rum, Madj),
	sused(Madj, Hrv), sused(Hrv, Bih).
boja(zuta).
boja(plava).
boja(crvena).
sused(X,Y):- boja(X), boja(Y), X \== Y.

% ======================================================================================
% Jadna macka Tuna
% 
% Ko je udario macku Tunu?
% Macka je zivotinja.
% Vlasnik psa voli zivotinje.
% Janko ima psa. Marko nema psa.
% Ne bi udario zivotinju ko voli zivotinje.
% Macku bi udario onaj koji bi je mozda udario i nije da je ne bi udario
% ======================================================================================

macka(tuna).
vlasnikpsa(janko).
mozda_udario(marko, tuna).
mozda_udario(janko, tuna).

zivotinja(X):- macka(X).
voli_zivotinje(X):- vlasnikpsa(X).
ne_bi_udario_zivotinju(X,Y):- voli_zivotinje(X), zivotinja(Y).
udario_macku(X, Y):- mozda_udario(X, Y), \+(ne_bi_udario_zivotinju(X,Y)).


% ======================================================================================
% Svi osim petra poznaju osobu koja je visa od njih.
% Roditelj je visi od deteta.
% ======================================================================================

izuzetak(petar).
roditelj(cale,cera).
visi(X, Y):- roditelj(X,Y).
poznaje_visu_osobu(X):- \+(izuzetak(X)).


