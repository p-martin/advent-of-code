use std::io::{BufReader, BufRead};
use std::fs::File;

const OPENING: &str = "([{<";
const CLOSING: &str = ")]}>";


fn main() {
    let lines: Vec<_> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .collect();

    let mut scores = vec![];
    for line in lines.iter() {
        let mut stack = vec![];
        let mut corrupt = false;
        for b in line.chars() {
            if let Some(i) = OPENING.find(b) {
                stack.push(CLOSING.as_bytes()[i] as char);
            } else if stack.is_empty() || stack.pop().unwrap() != b {
                corrupt = true;
                break;
            }
        }
        if !corrupt {
            let mut score = 0;
            stack.reverse();
            for &b in stack.iter() {
                score = 5 * score + 1 + CLOSING.find(b).unwrap();
            }
            scores.push(score);
        }
    }

    scores.sort();
    let result = scores[scores.len() / 2];
    println!("result = {result:?}");
}
