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
  list($A, $B) = lmis();
  println(sprintf("%.3f", $B/$A));
}

main();
