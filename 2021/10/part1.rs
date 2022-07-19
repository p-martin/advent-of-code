use std::io::{BufReader, BufRead};
use std::fs::File;

const OPENING: &str = "([{<";
const CLOSING: &str = ")]}>";


fn main() {
    let lines: Vec<_> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .collect();

    let mut result = 0u64;
    for line in lines.iter() {
        let mut stack = vec![];
        for b in line.chars() {
            if let Some(i) = OPENING.find(b) {
                stack.push(CLOSING.as_bytes()[i] as char);
            } else if stack.is_empty() || stack.pop().unwrap() != b {
                result += [3, 57, 1197, 25137][CLOSING.find(b).unwrap()];
                break;
            }
        }
    }

    println!("result = {result:?}");
}
