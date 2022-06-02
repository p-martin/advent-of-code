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
    let mut oxylines = lines.to_vec();
    let mut co2lines = lines.to_vec();
    for i in 0..num_cols {
        if oxylines.len() > 1 {
            let (ones, zeros) = get_bit_counts(&oxylines, i);
            oxylines = oxylines.into_iter()
                .filter(|line| line[i..=i].parse::<i32>().unwrap() == (ones >= zeros) as i32)
                .collect();
        }
        if co2lines.len() > 1 {
            let (ones, zeros) = get_bit_counts(&co2lines, i);
            co2lines = co2lines.into_iter()
                .filter(|line| line[i..=i].parse::<i32>().unwrap() == (ones < zeros) as i32)
                .collect();
        }
    }
    let oxygen = i32::from_str_radix(oxylines.first().unwrap(), 2).unwrap();
    let co2 = i32::from_str_radix(co2lines.first().unwrap(), 2).unwrap();

    let result = oxygen * co2;
    println!("result = {result:?}");
}
