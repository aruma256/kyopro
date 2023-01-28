// use itertools::Itertools;
use proconio::input;
// use proconio::marker::*;

fn main() {
    input! {
        _n: usize,
        s: String,
    }
    println!("{}", s.replace("na", "nya"));
}
