#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

fn main() {
    input! {
        n: usize,
        a: [Chars; n],
    }
    let get_pos = |r: usize, c: usize| -> (usize, usize) {
        if r == 0 {
            if c == 0 {
                (1, 0)
            } else {
                (0, c - 1)
            }
        } else if r == n-1 {
            if c == n-1 {
                (n-2, n-1)
            } else {
                (n-1, c + 1)
            }
        } else if c == 0 {
            (r + 1, 0)
        } else if c == n-1 {
            (r - 1, n-1)
        } else {
            (r, c)
        }
    };

    for r in 0..n {
        for c in 0..n {
            let (r, c) = get_pos(r, c);
            print!("{}", a[r][c]);
        }
        println!();
    }
}
