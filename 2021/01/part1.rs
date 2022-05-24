use std::io::{BufReader, BufRead};
use std::fs::File;

fn main() {
    let nums: Vec<_> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .flat_map(|s| s.parse::<i32>())
        .collect();

    let result: i32 = nums
        .windows(2)
        .map(|w| match w {
            [a, b] if a < b => 1,
            _ => 0,
        })
        .sum();

    println!("result = {result:?}");
}
