use std::fs::read_to_string;
use std::collections::HashSet;


fn main() {
    let content = read_to_string("input").unwrap();

    let mut east: HashSet<(i32, i32)> = HashSet::new();
    let mut south: HashSet<(i32, i32)> = HashSet::new();
    let mut h = 0;
    let mut w = 0;
    for (y, line) in content.trim().split('\n').enumerate() {
        h += 1;
        w = line.len() as i32;
        for (x, c) in line.chars().enumerate() {
            match c {
                '>' => east.insert((x as i32, y as i32)),
                'v' => south.insert((x as i32, y as i32)),
                _ => false,
            };
        }
    }

    let mut step = 0;
    let mut ch = true;
    while ch {
        ch = false;
        step += 1;
        let mut neweast: HashSet<(i32, i32)> = HashSet::new();
        for &(x, y) in east.iter() {
            let tx = (x + 1) % w;
            if east.contains(&(tx, y)) || south.contains(&(tx, y)) {
                neweast.insert((x, y));
            } else {
                neweast.insert((tx, y));
                ch = true;
            }
        }
        east = neweast;
        let mut newsouth: HashSet<(i32, i32)> = HashSet::new();
        for &(x, y) in south.iter() {
            let ty = (y + 1) % h;
            if east.contains(&(x, ty)) || south.contains(&(x, ty)) {
                newsouth.insert((x, y));
            } else {
                newsouth.insert((x, ty));
                ch = true;
            }
        }
        south = newsouth;
    }

    println!("result = {:?}", step);
}
