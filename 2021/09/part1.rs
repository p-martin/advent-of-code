use std::io::{BufReader, BufRead};
use std::fs::File;


fn main() {
    let field: Vec<Vec<_>> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .map(|s| s.chars().map(|c| c.to_digit(10).unwrap()).collect::<Vec<_>>())
        .collect();

    let mut result = 0;
    let h = field.len();
    let w = field[0].len();
    for (y, line) in field.iter().enumerate() {
        for (x, &level) in line.iter().enumerate() {
            if (x == 0 || level < field[y][x - 1]) &&
                (x == w - 1 || level < field[y][x + 1]) &&
                (y == 0 || level < field[y - 1][x]) &&
                (y == h - 1 || level < field[y + 1][x])
            {
                result += 1 + level;
            }
        }
    }

    println!("result = {result:?}");
}
