--Find the largest palindrome made from the product of two-digit numbers

def isPalandrome (n : Nat) : Bool :=
  let s := toString n
  s.data == s.data.reverse

