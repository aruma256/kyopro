#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

fn main() {
    input! {
        a: usize,
        b: usize,
    }
    if a + 1 == b && a % 3 != 0 {
        println!("Yes");
    } else {
        println!("No");
    }
}
