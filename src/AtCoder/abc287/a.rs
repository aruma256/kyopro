#![allow(unused_imports)]
use std::collections::*;
use itertools::Itertools;
use proconio::*;
use proconio::marker::*;

fn main() {
    input! {
        n: usize,
        ss: [String;n],
    }
    let mut count_for: usize = 0;
    let mut count_against: usize = 0;
    //
    for s in ss {
        if s == "For" {
            count_for += 1;
        } else {
            count_against += 1;
        }
    }
    if count_for > count_against {
        println!("Yes");
    } else {
        println!("No");
    }
}
