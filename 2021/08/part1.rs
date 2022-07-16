use std::io::{BufReader, BufRead};
use std::fs::File;
use std::collections::HashMap;


fn main() {
    let easy_digits: HashMap<usize, i32> = HashMap::from([(2, 1), (4, 4), (3, 7), (7, 8)]);
    let mut result = 0;
    for line in BufReader::new(File::open("input").unwrap()).lines().flatten() {
        let parts: Vec<_> = line.split(" | ").collect();
        if let [_left, right] = parts[..] {
            for group in right.trim().split(' ') {
                if easy_digits.contains_key(&group.len()) {
                    result += 1;
                }
            }
        }
    }

    println!("result = {result:?}");
}
