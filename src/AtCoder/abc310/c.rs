#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

#[fastout]
fn main() {
    input! {
        N: usize,
        S: [Chars; N],
    }
    // Sの各要素について、そのままと反転した文字列で辞書順で小さい方を選び、HashSetに格納する
    let mut set = HashSet::new();
    for i in 0..N {
        let mut s = S[i].clone();
        let mut s_rev = S[i].clone();
        s_rev.reverse();
        if s < s_rev {
            set.insert(s);
        } else {
            set.insert(s_rev);
        }
    }
    // HashSetの要素数を出力する
    println!("{}", set.len());
}
