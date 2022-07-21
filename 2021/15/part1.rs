use std::fs::read_to_string;
use std::collections::{HashMap, HashSet};


fn main() {
    let content = read_to_string("input").unwrap();

    let mut field = HashMap::new();
    for (y, line) in content.trim().split('\n').enumerate() {
        for (x, c) in line.chars().enumerate() {
            field.insert((x as i32, y as i32), c.to_digit(10).unwrap() as i32);
        }
    }
    let tx = field.keys().map(|p| p.0).max().unwrap();
    let ty = field.keys().map(|p| p.1).max().unwrap();

    let mut dists = HashMap::from([((0, 0), 0)]);
    let mut ff = HashSet::from([(0, 0)]);
    let mut ch = true;
    while ch && ff.len() > 0 {
        ch = false;
        let mut newff = HashSet::new();
        for &(x, y) in ff.iter() {
            let olddist = *dists.get(&(x, y)).or(Some(&1_000_000)).unwrap();
            for (dx, dy) in [(-1, 0), (0, -1), (1, 0), (0, 1)] {
                let nx = x + dx;
                let ny = y + dy;
                if field.contains_key(&(nx, ny)) {
                    let newdist = olddist + *field.get(&(nx, ny)).unwrap();
                    if !dists.contains_key(&(nx, ny)) || newdist < *dists.get(&(nx, ny)).unwrap() {
                        dists.insert((nx, ny), newdist);
                        newff.insert((nx, ny));
                        ch = true;
                    }
                }
            }
        }
        ff = newff;
    }

    let result = *dists.get(&(tx, ty)).unwrap();
    println!("result = {result:?}");
}
