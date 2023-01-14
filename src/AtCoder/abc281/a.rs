fn main() {
    let mut buf = String::new();
    std::io::stdin().read_line(&mut buf).expect("E0");
    let n: i32 = buf.trim().parse().expect("E1");
    let mut i = n;
    while i >= 0 {
        println!("{}", i);
        i -= 1;
    }
}
