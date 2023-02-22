<?php
fscanf(STDIN, "%d %d", $N, $X);
$P = array_map('intval', explode(" ", trim(fgets(STDIN))));
for ($k=0;$k<$N;$k++) {
  if ($P[$k]===$X) {
    echo $k+1;
  }
}
