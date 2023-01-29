#![allow(unused_imports, non_snake_case)]
use std::collections::*;
use itertools::Itertools;
use proconio::input;
use proconio::marker::*;

fn main() {
    input! {
        N: usize,
        X: usize,
        AB: [(usize, usize); N],
    }
    let mut dp = vec![false; X + 1];
    dp[0] = true;
    for (price, count) in AB {
        let mut dpn = dp.to_vec();
        for x in 0..=X {
            if !dp[x] {
                continue;
            }
            for mul in 1..=count {
                let nx = x + price * mul;
                if nx > X {
                    break;
                }
                dpn[nx] = true;
            }
        }
        dp = dpn;
    }
    if dp[X] {
        println!("Yes");
    } else {
        println!("No");
    }
    
}
