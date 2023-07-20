#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

fn main() {
    input! {
        N: usize,
        P: usize,
        Q: usize,
        D: [usize; N],
    }
    // Dの要素の最小値を求める
    let mut minD = D[0];
    for i in 1..N {
        minD = std::cmp::min(minD, D[i]);
    }
    // Q+minD と P の小さい方を出力する
    println!("{}", std::cmp::min(Q + minD, P)); 
}
