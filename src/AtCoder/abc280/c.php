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
  $S = input() . " ";
  $T = input();
  for ($i=0; $i < strlen($S); $i++) { 
    if ($S[$i] !== $T[$i]) {
      println($i + 1);
      return;
    }
  }
}

main();
