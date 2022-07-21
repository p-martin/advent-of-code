use std::fs::read_to_string;
use std::collections::HashMap;
use std::iter::FromIterator;


fn main() {
    let content = read_to_string("input").unwrap();

    let blocks: Vec<_> = content.trim().split("\n\n").collect();
    let mut pairs = HashMap::new();
    for (a, b) in blocks[0].chars().zip(blocks[0].chars().skip(1)) {
        *pairs.entry(String::from_iter([a, b])).or_insert(0) += 1;
    }
    let mut rules = HashMap::new();
    for line in blocks[1].split('\n') {
        let parts: Vec<_> = line.split(" -> ").collect();
        rules.insert(parts[0].to_string(), parts[1].chars().next().unwrap());
    }

    for _ in 1..=10 {
        let mut newpairs = HashMap::new();
        for (pair, &count) in pairs.iter() {
            if let [a, b] = pair.chars().collect::<Vec<_>>()[..2] {
                let &c = rules.get(pair).unwrap();
                *newpairs.entry(String::from_iter([a, c])).or_insert(0) += count;
                *newpairs.entry(String::from_iter([c, b])).or_insert(0) += count;
            }
        }
        pairs = newpairs;
    }
    let mut counts = HashMap::new();
    for (pair, &count) in pairs.iter() {
        if let [a, b] = pair.chars().collect::<Vec<_>>()[..2] {
            *counts.entry(a).or_insert(0) += count;
            *counts.entry(b).or_insert(0) += count;
        }
    }

    let result: u64 = (counts.values().max().unwrap()+1)/2 - (counts.values().min().unwrap()+1)/2;
    println!("result = {result:?}");
}
