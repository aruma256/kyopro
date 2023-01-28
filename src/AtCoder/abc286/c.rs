#![allow(unused_imports)]
use std::collections::*;
use itertools::Itertools;
use proconio::input;
use proconio::marker::*;

fn main() {
    input! {
        n: usize,
        a: usize,
        b: usize,
        s: Chars,
    }
    let mut ans = std::usize::MAX;
    let mut dq = VecDeque::from(s);
    for i in 0..n {
        let mut score = i * a;
        for j in 0..(n/2) {
            if dq[j] != dq[n-1-j] {
                score += b;
            }
        }
        ans = ans.min(score);
        let c = dq.pop_front().unwrap();
        dq.push_back(c)
    }
    println!("{}", ans);
}
