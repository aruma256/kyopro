FROM rust:1.66.1
RUN cargo install cargo-compete\
    && rustup install 1.42.0
