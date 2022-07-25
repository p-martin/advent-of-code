use std::io::{BufReader, BufRead};
use std::fs::File;


fn main() {
    let lines: Vec<_> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .collect();
    let mut p1: i32 = lines[0].split(": ").last().unwrap().parse().unwrap();
    let mut p2: i32 = lines[1].split(": ").last().unwrap().parse().unwrap();

    let mut r = 0;
    let mut sc1 = 0;
    let mut sc2 = 0;
    'outer: loop {
        for i in 0..6 {
            r += 1;
            let val = (r - 1) % 100 + 1;
            if i < 3 {
                p1 = (p1 + val - 1) % 10 + 1;
            } else {
                p2 = (p2 + val - 1) % 10 + 1;
            }
            if i == 2 {
                sc1 += p1;
            } else if i == 5 {
                sc2 += p2;
            }
            if sc1 > 1000 || sc2 > 1000 {
                break 'outer;
            }
        }
    }

    let result = (sc1.min(sc2)) * r;
    println!("result = {result:?}");
}
