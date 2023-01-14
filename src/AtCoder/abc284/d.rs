use proconio::input;
use num_integer::Roots;

fn main() {
    input! {
        t: usize,
        ns: [usize; t],
    }
    for n in ns {
        for i in 2.. {
            if n%i == 0 {
                if n%(i*i) == 0 {
                    println!("{} {}", i, n/i/i);
                } else {
                    println!("{} {}", (n/i).sqrt(), i);
                }
                break;
            }
        }
    }
}
