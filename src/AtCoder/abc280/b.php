<?php
function input() {
  return trim(fgets(STDIN));
}

function ii() {
  return (int)input();
}

function lmis() {
  return array_map('intval', explode(" ", input()));
}

function println($str) {
  print($str . "\n");
}

function main() {
  $N = ii();
  $A = lmis();
  $ans = [$A[0]];
  for ($i=1; $i < $N; $i++) { 
    array_push($ans, $A[$i] - $A[$i - 1]);
  }
  println(implode(" ", $ans));
}

main();
