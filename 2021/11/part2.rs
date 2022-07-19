use std::io::{BufReader, BufRead};
use std::fs::File;
use std::collections::{HashMap, HashSet};


fn main() {
    let lines: Vec<_> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .collect();

    let h = lines.len();
    let w = lines[0].len();
    let mut field = HashMap::new();
    for (y, line) in lines.iter().enumerate() {
        for (x, c) in line.chars().enumerate() {
            field.insert((x, y), c.to_digit(10).unwrap());
        }
    }

    let mut step = 0;
    loop {
        step += 1;
        let mut newfield = HashMap::new();
        let mut flashing = HashSet::new();
        for (&(x, y), &value) in field.iter() {
            let newvalue = value + 1;
            newfield.insert((x, y), newvalue);
            if newvalue > 9 {
                flashing.insert((x, y));
            }
        }
        while flashing.len() > 0 {
            let mut newflashing = HashSet::new();
            for &(x, y) in flashing.iter() {
                for nx in (if x > 0 {x - 1} else {x})..=(if x < w - 1 {x + 1} else {x}) {
                    for ny in (if y > 0 {y - 1} else {y})..=(if y < h - 1 {y + 1} else {y}) {
                        if nx != x || ny != y {
                            let newvalue = newfield.get(&(nx, ny)).unwrap() + 1;
                            newfield.insert((nx, ny), newvalue);
                            if newvalue == 10 {
                                newflashing.insert((nx, ny));
                            }
                        }
                    }
                }
            }
            flashing = newflashing;
        }
        let mut allflashed = true;
        for (&(x, y), &value) in newfield.iter() {
            if value <= 9 {
                allflashed = false;
            }
            field.insert((x, y), if value > 9 {0} else {value});
        }
        if allflashed {
            break;
        }
    }

    println!("result = {step:?}");
}
