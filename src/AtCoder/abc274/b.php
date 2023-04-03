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
  list($H, $W) = lmis();
  $C = [];
  for ($h=0; $h < $H; $h++) {
    $C[] = input();
  }
  $ans = [];
  for ($w=0; $w < $W; $w++) {
    $count = 0;
    for ($h=0; $h < $H; $h++) {
      if ($C[$h][$w]==='#') {
        $count += 1;
      }
    }
    $ans[] = $count;
  }
  println(implode(' ', $ans));
}

main();
