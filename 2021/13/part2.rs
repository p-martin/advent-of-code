use std::fs::read_to_string;
use std::collections::HashSet;


fn main() {
    let content = read_to_string("input").unwrap();

    let blocks: Vec<_> = content.trim().split("\n\n").collect();
    let mut dots = HashSet::new();
    for line in blocks[0].split('\n') {
        let parts: Vec<_> = line
            .split(',')
            .map(|s| s.parse::<i32>().unwrap())
            .collect();
        if let [x, y] = parts[..] {
            dots.insert((x, y));
        }
    }

    for cmd in blocks[1].split('\n') {
        let fold = cmd.split('=').skip(1).next().unwrap().parse::<i32>().unwrap();
        let mut newdots = HashSet::new();
        if cmd.contains("x=") {
            for &(x, y) in dots.iter() {
                newdots.insert((if x < fold {x} else {2 * fold - x}, y));
            }
        } else {
            for &(x, y) in dots.iter() {
                newdots.insert((x, if y < fold {y} else {2 * fold - y}));
            }
        }
        dots = newdots;
    }

    let minx = dots.iter().map(|p| p.0).min().unwrap();
    let maxx = dots.iter().map(|p| p.0).max().unwrap();
    let miny = dots.iter().map(|p| p.1).min().unwrap();
    let maxy = dots.iter().map(|p| p.1).max().unwrap();
    let mut result = "\n".to_string();
    for y in miny..=maxy {
        for x in minx..=maxx {
            result += if dots.contains(&(x, y)) { "█" } else { "." };
        }
        result += "\n";
    }
    println!("result = {result}");
}
