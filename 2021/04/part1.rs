use std::fs::read_to_string;


fn is_board_finished(b: &Vec<i32>) -> bool {
    (0..5).any(|y| b[5*y..5*y+5].iter().all(|&n| n < 0)) ||
        (0..5).any(|x| b.iter().skip(x).step_by(5).all(|&n| n < 0))
}


fn main() {
    let content = read_to_string("input").unwrap();
    let blocks: Vec<_> = content.trim().split("\n\n").collect();

    let numbers: Vec<_> = blocks[0].split(',')
        .flat_map(|s| s.parse::<i32>())
        .collect();
    let mut boards: Vec<Vec<i32>> = blocks.iter()
        .skip(1)
        .map(|&s| s.split_whitespace().map(|n| n.parse::<i32>().unwrap()).collect::<Vec<i32>>())
        .collect();

    for &num in numbers.iter() {
        boards = boards.iter()
            .map(|b| b.iter().map(|&n| if n == num {-1} else {n}).collect())
            .collect();
        for b in boards.iter() {
            if is_board_finished(b) {
                let result = num * b.iter()
                    .map(|&n| if n < 0 {0} else {n})
                    .sum::<i32>();
                println!("result = {result:?}");
                return;
            }
        }
    }
    panic!("All numbers drawn, but no board finished.");
}
