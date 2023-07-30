#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

#[fastout]
fn main() {
    input! {
        S: String,
    }
    // Sが ACE、BDF、CEG、DFA、EGB、FAC、GBD のいずれかに等しいならYes
    if S == "ACE" || S == "BDF" || S == "CEG" || S == "DFA" || S == "EGB" || S == "FAC"  || S == "GBD" {
        println!("Yes");
    } else {
        println!("No");
    };
}
