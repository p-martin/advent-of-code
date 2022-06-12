use std::io::{BufReader, BufRead};
use std::fs::File;
use std::collections::HashMap;


fn main() {
    let lines: Vec<_> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .collect();

    let mut field = HashMap::new();
    for line in lines.iter() {
        let coords: Vec<_> = line
            .replace(" -> ", ",")
            .split(',')
            .map(|s| s.parse::<i32>().unwrap())
            .collect();
        if let &[x1, y1, x2, y2] = coords.as_slice() {
            let dx = (x2 - x1).signum();
            let dy = (y2 - y1).signum();
            if dx == 0 || dy == 0 {
                let mut x = x1 - dx;
                let mut y = y1 - dy;
                while x != x2 || y != y2 {
                    x += dx;
                    y += dy;
                    *field.entry((x, y)).or_insert(0) += 1;
                }
            }
        }
    }

    let result = field.values()
        .filter(|&v| *v > 1)
        .count();
    println!("result = {result:?}");
}
