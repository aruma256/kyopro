#![allow(non_snake_case)]
#![allow(unused_imports)]
use proconio::{fastout, input, marker::Chars};
use std::collections::{BTreeSet, BinaryHeap, HashMap, HashSet, VecDeque};

fn main() {
    input! {
        HA: usize,
        WA: usize,
        A: [Chars; HA],
        HB: usize,
        WB: usize,
        B: [Chars; HB],
        HC: usize,
        WC: usize,
        C: [Chars; HC],
    }
    let mut a_black_count = 0;
    for y in 0..HA {
        for x in 0..WA {
            if A[y][x] == '#' {
                a_black_count += 1;
            }
        }
    }
    let mut b_black_count = 0;
    for y in 0..HB {
        for x in 0..WB {
            if B[y][x] == '#' {
                b_black_count += 1;
            }
        }
    }

    let cdx = 10;
    let cdy = 10;
    for adx in 0..=20 {
        for ady in 0..=20 {
            for bdx in 0..=20 {
                for bdy in 0..=20 {
                    let mut is_good = true;
                    let mut used_a_black_count = 0;
                    let mut used_b_black_count = 0;
                    for c_local_x in 0..WC {
                        for c_local_y in 0..HC {
                            let mut cell_color = '.';
                            if cdx + c_local_x >= adx && cdy + c_local_y >= ady {
                                let a_local_x = cdx + c_local_x - adx;
                                let a_local_y = cdy + c_local_y - ady;
                                if 0 <= a_local_x && a_local_x < WA && 0 <= a_local_y && a_local_y < HA {
                                    if A[a_local_y][a_local_x] == '#' {
                                        cell_color = '#';
                                        used_a_black_count += 1;
                                    }
                                }
                            }
                            if cdx + c_local_x >= bdx && cdy + c_local_y >= bdy {
                                let b_local_x = cdx + c_local_x - bdx;
                                let b_local_y = cdy + c_local_y - bdy;
                                if 0 <= b_local_x && b_local_x < WB && 0 <= b_local_y && b_local_y < HB {
                                    if B[b_local_y][b_local_x] == '#' {
                                        cell_color = '#';
                                        used_b_black_count += 1;
                                    }
                                }
                            }
                            if C[c_local_y][c_local_x] != cell_color {
                                is_good = false;
                                break;
                            }
                        }
                        if !is_good {
                            break;
                        }
                    }
                    if is_good && used_a_black_count == a_black_count && used_b_black_count == b_black_count {
                        println!("Yes");
                        return;
                    }
                }
            }
        }
    }
    println!("No");
}
