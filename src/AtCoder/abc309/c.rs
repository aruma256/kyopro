// written with GitHub Copilot

#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

fn main() {
    input! {
        n: usize,
        k: usize,
        mut ab: [(usize, usize); n],
    }
    // ab に (10^10, 0) を追加
    ab.push((1e10 as usize, 0));
    // abをaで昇順ソート
    ab.sort_by(|a, b| a.0.cmp(&b.0));
    // bの合計を計算
    let mut b_sum = 0;
    for i in 0..n {
        b_sum += ab[i].1;
    }
    let mut i = 0;
    let mut day = 1;
    let mut d = b_sum;
    // d>k である限りループ
    while d > k {
        d -= ab[i].1;
        day = ab[i].0 + 1;
        i += 1;
    }
    println!("{}", day);
}
