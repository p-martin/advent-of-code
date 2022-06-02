use std::io::{BufReader, BufRead};
use std::fs::File;


fn get_bit_counts(lines: &Vec<String>, pos: usize) -> (usize, usize) {
    let ones = lines.iter()
        .filter(|&line| line[pos..=pos].parse::<i32>().unwrap() == 1)
        .count();
    (ones, lines.len() - ones)
}


fn main() {
    let lines: Vec<_> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .collect();

    let num_cols = lines[0].len();
    let mut gamma = 0;
    let mut epsilon = 0;
    for i in 0..num_cols {
        gamma <<= 1;
        epsilon <<= 1;
        let (ones, zeros) = get_bit_counts(&lines, i);
        gamma += (ones > zeros) as i32;
        epsilon += (ones <= zeros) as i32;
    }

    let result = gamma * epsilon;
    println!("result = {result:?}");
}
