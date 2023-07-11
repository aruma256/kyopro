#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

fn main() {
    input! {
        N: usize,
        M: usize,
        P: [usize; N-1],
        xy: [(usize, isize); M],
    }
    let mut dp = vec![0; N+1];
    for (x, y) in xy {
        dp[x] = std::cmp::max(dp[x], y + 1);
    }
    for i in 2..=N {
        dp[i] = std::cmp::max(dp[i], dp[P[i-2]] - 1);
    }
    let mut ans = 0;
    // dp配列の1からNまでのうち、正の値の個数を数える
    for i in 1..=N {
        if dp[i] > 0 {
            ans += 1;
        }
    }
    println!("{}", ans);
}