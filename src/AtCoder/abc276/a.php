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
  $S = input();
  $pos = strrpos($S, "a");
  println($pos !== false ? $pos + 1 : -1);
}

main();
