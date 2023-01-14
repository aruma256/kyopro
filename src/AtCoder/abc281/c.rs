use proconio::*;
use proconio::marker::*;

fn main() {
    input! {
        n: usize,
        mut t: usize,
        vec_a: [usize; n],
    }
    t %= vec_a.iter().sum::<usize>();
    for (i, a) in vec_a.iter().enumerate() {
        if t < *a {
            println!("{} {}", i+1, t);
            return;
        }
        t -= *a;
    }
}
