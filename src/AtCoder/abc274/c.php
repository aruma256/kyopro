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
  $ans = [0, 0];
  foreach ($A as $a) {
    $ans[] = $ans[$a] + 1;
    $ans[] = $ans[$a] + 1;
  }
  array_shift($ans);
  foreach ($ans as $ansElem) {
    println($ansElem);
  }
}

main();
