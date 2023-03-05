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
  list($N, $Q) = lmis();
  $d = [];
  for ($i=0; $i < $Q; $i++) { 
    list($type, $x) = lmis();
    if ($type <= 2) {
      $d[$x] += $type;
    } else {
      println($d[$x] >= 2 ? "Yes" : "No");
    }
  }
}

main();
