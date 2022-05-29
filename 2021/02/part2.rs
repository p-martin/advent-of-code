use std::io::{BufReader, BufRead};
use std::fs::File;

fn main() {
    let lines: Vec<_> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .collect();

    let mut x = 0;
    let mut a = 0;
    let mut y = 0;

    for line in lines.iter() {
        let parts: Vec<_> = line.split(' ').collect();
        match parts[..] {
            ["forward", val] => {
                let dist = val.parse::<i32>().unwrap();
                x += dist;
                y += a * dist;
            },
            ["down", val] => a += val.parse::<i32>().unwrap(),
            ["up", val] => a -= val.parse::<i32>().unwrap(),
            _ => panic!("invalid line {:?}", line),
        }
    }

    let result = x * y;
    println!("result = {result:?}");
}
