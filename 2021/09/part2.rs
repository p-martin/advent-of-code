use std::io::{BufReader, BufRead};
use std::fs::File;
use std::collections::HashSet;


fn main() {
    let field: Vec<Vec<_>> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .map(|s| s.chars().map(|c| c.to_digit(10).unwrap()).collect::<Vec<_>>())
        .collect();

    let mut low_points = HashSet::new();
    let h = field.len();
    let w = field[0].len();
    for (y, line) in field.iter().enumerate() {
        for (x, &level) in line.iter().enumerate() {
            if (x == 0 || level < field[y][x - 1]) &&
                (x == w - 1 || level < field[y][x + 1]) &&
                (y == 0 || level < field[y - 1][x]) &&
                (y == h - 1 || level < field[y + 1][x])
            {
                low_points.insert((x, y));
            }
        }
    }
    let mut basins = Vec::new();
    for &(sx, sy) in low_points.iter() {
        let mut seen = HashSet::new();
        let mut ff = HashSet::from([(sx, sy)]);
        while ff.len() > 0 {
            let mut newff = HashSet::new();
            for &(x, y) in ff.iter() {
                if 0 < x && field[y][x - 1] < 9 && !seen.contains(&(x - 1, y)) {
                    newff.insert((x - 1, y));
                }
                if x < w - 1 && field[y][x + 1] < 9 && !seen.contains(&(x + 1, y)) {
                    newff.insert((x + 1, y));
                }
                if 0 < y && field[y - 1][x] < 9 && !seen.contains(&(x, y - 1)) {
                    newff.insert((x, y - 1));
                }
                if y < h - 1 && field[y + 1][x] < 9 && !seen.contains(&(x, y + 1)) {
                    newff.insert((x, y + 1));
                }
                seen.insert((x, y));
            }
            ff = newff;
        }
        basins.push(seen.len());
    }

    basins.sort();
    basins.reverse();
    let result: usize = basins.iter().take(3).product();
    println!("result = {result:?}");
}
