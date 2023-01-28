use itertools::Itertools;
use proconio::input;
use proconio::marker::*;

fn main() {
    input! {
        n: usize,
        mut p: usize,
        mut q: usize,
        mut r: usize,
        mut s: usize,
        mut a: [usize; n],
    }
    p -= 1;
    q -= 1;
    r -= 1;
    s -= 1;

    for d in 0..=(q-p) {
        a.swap(p+d, r+d);
    }
    println!("{}", a.iter().join(" "));
}
