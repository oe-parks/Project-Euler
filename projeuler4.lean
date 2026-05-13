--Find the largest palindrome made from the product of two-digit numbers

def isPalandrome (n : Nat) : Bool :=
  let s := toString n
  s.toList == s.toList.reverse

def largestPalindrome : Nat :=
  let palindromes := (List.range 900).flatMap (fun i =>
    (List.range 900).map fun j =>
      (i + 100) * (j + 100))
  (palindromes.filter isPalandrome).foldl Nat.max 0

#eval largestPalindrome
