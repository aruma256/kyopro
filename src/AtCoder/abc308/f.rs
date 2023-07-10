#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};
 
fn main() {
    input! {
        n: usize,
        m: usize,
        mut p: [isize; n], // 商品価格リスト
        l: [isize; m], // 最低価格リスト
        d: [isize; m], // 割引額リスト
    }
    // 同じインデックスのlとdからクーポン情報をリストにする
    let mut coupons = vec![];
    for i in 0..m {
        coupons.push((l[i], -d[i]));
    }
    // クーポンを最低価格と割引額の昇順にソートする
    coupons.sort();
    // 商品価格を昇順にソートする
    p.sort();
    // 優先度付きキューを用意する
    let mut available_coupons = BinaryHeap::new();
    //
    let mut ans = 0;
    let mut coupon_i = 0;
    for i in 0..n {
        let price = p[i];
        // 利用可能なクーポンを優先度付きキューに追加する
        while coupon_i < m && coupons[coupon_i].0 <= price {
            available_coupons.push(-coupons[coupon_i].1);
            coupon_i += 1;
        }
        // 利用可能なクーポンがあれば、最も割引額の大きいクーポンを使う
        if let Some(discount) = available_coupons.pop() {
            ans += price - discount;
        } else {
            ans += price;
        }
    }
    println!("{}", ans);
}
