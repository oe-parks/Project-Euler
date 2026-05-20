def answer : Nat :=
  (List.range 20).foldl (fun acc i => Nat.lcm acc (i + 1)) 1

#eval answer
