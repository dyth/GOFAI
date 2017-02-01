datatype 'a square = X | O | E;
datatype 'a tree   = Lf of 'a square
                   | Tr of 'a tree list;

val board = [E, E, E, E, E, E, E, E, E]; 

exception INVALID;

(* set nth element in (H::T) to sq *)
fun set (H::T) sq 0 = if H = E then (sq::T) else raise INVALID
  | set (H::T) sq n = H :: (set T sq (n-1));

(* check if current state denotes a winner *)
fun winner [a, b, c, d, e, f, g, h, i] =
  if (a = b) andalso (b = c) andalso (not (a = E)) then a
  else if (d = e) andalso (e = f) andalso (not (d = E)) then d
  else if (g = h) andalso (h = i) andalso (not (g = E)) then g
  else if (a = d) andalso (d = g) andalso (not (a = E)) then a
  else if (b = e) andalso (e = h) andalso (not (b = E)) then b
  else if (c = f) andalso (f = i) andalso (not (c = E)) then c
  else if (a = e) andalso (e = i) andalso (not (a = E)) then a
  else if (c = e) andalso (e = g) andalso (not (c = E)) then c
  else E;

(* nextturn: change player *)
fun nextturn sq = case sq of X => O | O => X;

(* create game tree from each initial move
   playall: from current board, play all possible positions *)
fun moveall bd sq =
  let fun playall bd sq = List.mapPartial (fn x => SOME (set bd sq x) handle INVALID => NONE) [0,1,2,3,4,5,6,7,8]
  in map (fn n => if (not (E = winner n)) then Lf(winner n)
				  else if (List.exists (fn x => x = E) n)
				  then Tr(moveall n (nextturn sq))
				  else Lf E)
		 (playall bd sq)
  end;

(* return next move based on most probable wins
   wins: number of times sq has won
   games: number of possible games
   greatest: find index of greatest element in the list *)
fun nextmove bd sq =
  let fun wins (Lf x) sq = if (x = sq) then 1.0 else 0.0
		| wins (Tr []) sq = 0.0
		| wins (Tr (H::T)) sq = (wins H sq) + (wins (Tr T) sq);
	  fun games (Lf _) = 1.0
		| games (Tr []) = 0.0
		| games (Tr (H::T)) = (games H) + (games (Tr T));
	  fun greatest [] n v m = m
		| greatest (H::T) n v m = if (v < H) then greatest T (n+1) H n
								  else greatest T (n+1) v m
  in set bd sq (greatest (map (fn x => (wins x sq) / (games x)) (moveall bd sq)) 0 0.0 0)
  end;

(* player move bd, computer response *)
fun move bd sq n = nextmove (set bd sq n) (nextturn sq);
