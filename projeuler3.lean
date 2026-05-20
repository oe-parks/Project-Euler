def isPrime (n : Nat) : Bool :=
  if n < 2 then false
  else (List.range (n - 2)).all (fun m => n % (m + 2) != 0)

def primeFactorAux (n : Nat) (d : Nat) (best : Nat) : Nat :=
  if d * d > n then
    if n > 1 then n else best
  else if n % d == 0 then
    primeFactorAux (n / d) d d
  else
    primeFactorAux n (d + 1) best
termination_by (n, n - d)

def largestPrimeFactor (n : Nat) : Nat :=
  primeFactorAux n 2 1

#eval! largestPrimeFactor 600851475143
