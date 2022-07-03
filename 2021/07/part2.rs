use std::fs::read_to_string;


fn series_sum(n: i32) -> i32 {
    (n + 1) * n / 2
}


fn main() {
    let positions: Vec<_> = read_to_string("input").unwrap().trim()
        .split(',')
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    let mut result = i32::MAX;
    for p in *positions.iter().min().unwrap()..=*positions.iter().max().unwrap() {
        result = result.min(positions.iter().map(|&pp| series_sum((pp - p).abs())).sum());
    }

    println!("result = {result:?}");
}
