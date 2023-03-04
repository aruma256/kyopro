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
  list($H, $W) = lmis();
  $ans = 0;
  for ($i=0; $i < $H; $i++) { 
    $line = input();
    $ans += substr_count($line, "#");
  }
  echo $ans;
}

main();
