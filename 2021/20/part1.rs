use std::fs::read_to_string;
use std::collections::HashSet;


fn main() {
    let content = read_to_string("input").unwrap();
    let blocks: Vec<_> = content.trim().split("\n\n").collect();

    let mut lightpx = HashSet::new();
    for (y, line) in blocks[1].lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            if c == '#' {
                lightpx.insert((x as i32, y as i32));
            }
        }
    }

    for i in 1..=2 {
        let mut newlightpx = HashSet::new();
        let minx = lightpx.iter().map(|&p| p.0).min().unwrap();
        let miny = lightpx.iter().map(|&p| p.1).min().unwrap();
        let maxx = lightpx.iter().map(|&p| p.0).max().unwrap();
        let maxy = lightpx.iter().map(|&p| p.1).max().unwrap();

        for y in miny-1..=maxy+1 {
            for x in minx-1..=maxx+1 {
                let mut val = 0;
                for dy in -1..=1 {
                    for dx in -1..=1 {
                        val <<= 1;
                        if &blocks[0][0..=0] == "." || (minx <= x+dx && x+dx <= maxx && miny <= y+dy && y+dy <= maxy) {
                            if lightpx.contains(&(x+dx, y+dy)) {
                                val |= 1;
                            }
                        } else if i % 2 == 0 {
                            val |= 1;
                        }
                    }
                }
                if &blocks[0][val..=val] == "#" {
                    newlightpx.insert((x, y));
                }
            }
        }
        lightpx = newlightpx;
    }

    let result = lightpx.len();
    println!("result = {result:?}");
}
