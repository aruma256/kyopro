use proconio::input;
use proconio::marker::Chars;
use itertools::*;

fn main() {
    input! {
        n: usize,
        m: usize,
        s: [Chars; n],
    }
    let mut ans = 0;
    for ij in (0..n).combinations(2) {
        let i = ij[0];
        let j = ij[1];
        let mut perfect = true;
        for t in 0..m {
            if s[i][t]=='x' && s[j][t]=='x' {
                perfect = false;
                break;
            }
        }
        if perfect {
            ans += 1;
        }
    }
    println!("{}", ans);
}
