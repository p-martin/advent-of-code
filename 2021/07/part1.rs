use std::fs::read_to_string;


fn main() {
    let positions: Vec<_> = read_to_string("input").unwrap().trim()
        .split(',')
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    let mut result = i32::MAX;
    for p in *positions.iter().min().unwrap()..=*positions.iter().max().unwrap() {
        result = result.min(positions.iter().map(|&pp| (pp - p).abs()).sum());
    }

    println!("result = {result:?}");
}
