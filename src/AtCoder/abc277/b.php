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

function main() {
  $N = ii();
  $d = [];
  for ($i=0; $i < $N; $i++) {
    $s = input();
    if (preg_match('/^[HDCS][A2-9TJQK]+$/', $s) && !$d[$s]) {
      $d[$s] = true;
    } else {
      echo "No";
      return;
    }
  }
  echo "Yes";
}

main();
