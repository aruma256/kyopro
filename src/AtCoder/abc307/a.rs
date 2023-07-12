#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

fn main() {
    input! {
        N: usize,
        A: [usize; N * 7],
    }
    // 7日ごとの合計をprintする
    for i in 0..N {
        let mut sum = 0;
        for j in 0..7 {
            sum += A[i * 7 + j];
        }
        print!("{} ", sum);
    }
}
