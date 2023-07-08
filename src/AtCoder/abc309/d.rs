// written with GitHub Copilot

#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

fn main() {
    input! {
        n1: usize,
        n2: usize,
        m: usize,
        ab: [(usize, usize); m], // 点aと点bを結ぶ無向辺
    }
    //
    let mut graph = vec![vec![]; n1 + n2 + 1];
    for (a, b) in ab {
        graph[a].push(b);
        graph[b].push(a);
    }
    // 点1からBFSし、深さの最大値を得る
    let mut max_depth_from_1 = 0;
    let mut visited = vec![false; n1 + n2 + 1];
    let mut queue = VecDeque::new();
    queue.push_back((1, 0));
    while let Some((node, depth)) = queue.pop_front() {
        if visited[node] {
            continue;
        }
        visited[node] = true;
        max_depth_from_1 = depth;
        for &next in &graph[node] {
            queue.push_back((next, depth + 1));
        }
    }
    // 点 N1+N2 からBFSし、深さの最大値を得る
    let mut max_depth_from_n1n2 = 0;
    let mut visited = vec![false; n1 + n2 + 1];
    let mut queue = VecDeque::new();
    queue.push_back((n1 + n2, 0));
    while let Some((node, depth)) = queue.pop_front() {
        if visited[node] {
            continue;
        }
        visited[node] = true;
        max_depth_from_n1n2 = depth;
        for &next in &graph[node] {
            queue.push_back((next, depth + 1));
        }
    }
    //
    println!("{}", max_depth_from_1 + max_depth_from_n1n2 + 1);
}
