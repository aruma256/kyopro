use proconio::input;
use proconio::marker::Chars;
// use itertools::*;

fn main() {
    input! {
        _n: usize,
        s: Chars,
    }
    let mut isin = false;
    for mut c in s {
        if c==',' {
            if !isin {
                c = '.';
            }
        } else if c=='"' {
            isin = !isin;
        }
        print!("{}", c);
    }
    println!("");
}
