#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

#[fastout]
fn main() {
    input! {
        S: Chars,
    }
    let count_max = S.len() + 1;
    let mut dp: Vec<usize> = vec![0; count_max];
    let mut dpn: Vec<usize> = vec![0; count_max];
    dp[0] = 1;
    for char_i in 0..S.len() {
        if S[char_i] == '(' {
            for count_i in 0..(count_max-1) {
                dpn[count_i + 1] += dp[count_i];
            }
        } else if S[char_i] == ')' {
            for count_i in 1..count_max {
                dpn[count_i - 1] += dp[count_i];
            }
        } else {
            for count_i in 0..(count_max-1) {
                dpn[count_i + 1] += dp[count_i];
            }
            for count_i in 1..count_max {
                dpn[count_i - 1] += dp[count_i];
            }
        }
        //
        for count_i in 0..count_max {
            dp[count_i] = dpn[count_i] % 998244353;
            dpn[count_i] = 0;
        }
    }
    println!("{}", dp[0]);
}
