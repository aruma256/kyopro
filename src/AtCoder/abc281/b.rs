use proconio::*;
use proconio::marker::*;

fn main() {
    input! {
        s: Chars,
    }
    if s.len() != 8 {
        println!("No");
        return;
    }
    let mut valid = true;
    valid &= s[0].is_ascii_uppercase();
    valid &= (s[1] != '0');
    valid &= s[1..=6].iter().all(|&c| c.is_ascii_digit());
    valid &= s[7].is_ascii_uppercase();

    if valid {
        println!("Yes");
    } else {
        println!("No");
    }
}
