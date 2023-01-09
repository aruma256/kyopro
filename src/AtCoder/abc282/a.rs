fn main() {
    proconio::input! {
        n: u8,
    }
    for i in 0..n {
        print!("{}", (('A' as u8) + i) as char);
    }
}
