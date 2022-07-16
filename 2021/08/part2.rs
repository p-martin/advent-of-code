use std::io::{BufReader, BufRead};
use std::fs::File;
use std::collections::{HashMap, HashSet};
use std::iter::FromIterator;


fn main() {
    let easy_digits: HashMap<usize, i32> = HashMap::from([(2, 1), (4, 4), (3, 7), (7, 8)]);
    let mut result = 0;
    for line in BufReader::new(File::open("input").unwrap()).lines().flatten() {
        let parts: Vec<_> = line.split(" | ").collect();
        if let [left, right] = parts[..] {
            let mut digits: HashMap<_, HashSet<_>> = HashMap::new();
            for group in left.trim().split(' ') {
                let dlen = group.len();
                if easy_digits.contains_key(&dlen) {
                    let &digit = easy_digits.get(&dlen).unwrap();
                    digits.entry(digit).or_insert(HashSet::from_iter(group.chars()));
                }
            }
            for group in left.trim().split(' ') {
                let hs = HashSet::from_iter(group.chars());
                match group.len() {
                    5 => {
                        if hs.intersection(digits.get(&7).unwrap()).count() == 3 {
                            digits.entry(3).or_insert(hs);
                        } else if hs.intersection(digits.get(&4).unwrap()).count() == 3 {
                            digits.entry(5).or_insert(hs);
                        } else {
                            digits.entry(2).or_insert(hs);
                        }
                    },
                    6 => {
                        if hs.intersection(digits.get(&4).unwrap()).count() == 4 {
                            digits.entry(9).or_insert(hs);
                        } else if hs.intersection(digits.get(&7).unwrap()).count() == 3 {
                            digits.entry(0).or_insert(hs);
                        } else {
                            digits.entry(6).or_insert(hs);
                        }
                    },
                    _ => {},
                }
            }
            let mut val = 0;
            for group in right.trim().split(' ') {
                let hs = HashSet::from_iter(group.chars());
                for (digit, hsd) in digits.iter() {
                    if hsd.eq(&hs) {
                        val = 10*val + digit;
                        break;
                    }
                }
            }
            result += val;
        }
    }

    println!("result = {result:?}");
}
