#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

#[fastout]
fn main() {
    let tak = "###.?????
###.?????
###.?????
....?????
?????????
?????....
?????.###
?????.###
?????.###";
    let tak = tak.split("\n").collect::<Vec<&str>>();
    input! {
        N: usize,
        M: usize,
        S: [Chars; N],
    }
    for start_h in 0..=(N-9) {
        for start_w in 0..=(M-9) {
            let mut ok = true;
            // tak と S を比較する
            for h in 0..9 {
                for w in 0..9 {
                    let tak_c = tak[h].chars().nth(w).unwrap();
                    if tak_c == '#' && S[start_h + h][start_w + w] == '#' {
                    }
                    else if tak_c == '.' && S[start_h + h][start_w + w] == '.' {
                    }
                    else if tak_c == '?' {
                    }
                    else {
                        ok = false;
                    }
                }
            }
            if ok {
                println!("{} {}", start_h+1, start_w+1);
            }
        }
    }
}
