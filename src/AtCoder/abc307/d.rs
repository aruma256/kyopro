#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

fn main() {
    input! {
        N: usize,
        S: Chars,
    }
    let mut ans = vec![];
    let mut level = 0;
    for c in S.iter() {
        if *c == ')' && level > 0 {
            // ansの最後の要素が'('になるまでpopする
            while ans[ans.len() - 1] != '(' {
                ans.pop();
            }
            ans.pop();
            level -= 1;
            continue;
        }
        ans.push(*c);
        if *c == '(' {
            level += 1;
        }
    }
    // ansが空ならばreturn
    if ans.is_empty() {
        return;
    }
    // ansを結合してprintする
    println!("{}", ans.iter().collect::<String>());
}
