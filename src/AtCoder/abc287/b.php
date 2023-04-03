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
  list($N, $M) = lmis();
  $s_parts = [];
  for ($i=0; $i < $N; $i++) { 
    $s_parts[] = substr(input(), 3, 6);
  }
  $t_array = [];
  for ($i=0; $i < $M; $i++) { 
    $t_array[] = input();
  }
  $ans = 0;
  foreach ($s_parts as $s_part) {
    if (in_array($s_part, $t_array)) {
      $ans += 1;
    }
  }
  println($ans);
}

main();
