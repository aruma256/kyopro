#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

fn main() {
    input! {
        N: usize,
        S: [Chars; N],
    }
    // 全てのSの組み合わせについて
    for i in 0..N {
        for j in 0..N {
            if i == j {
                continue;
            }
            // S[i] と S[j] の文字列を結合する
            let mut s = S[i].clone();
            s.extend(S[j].clone());
            // sが回文かどうかを判定する
            let mut is_palindrome = true;
            for char_i in 0..s.len() {
                if s[char_i] != s[s.len() - char_i - 1] {
                    is_palindrome = false;
                    break;
                }
            }
            // 回文ならば、"Yes"をprintして終了する
            if is_palindrome {
                println!("Yes");
                return;
            }
        }
    }
    // 全ての組み合わせについて回文が存在しない場合は"No"をprintする
    println!("No");
}
