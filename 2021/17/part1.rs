use std::fs::read_to_string;


fn get_max_y(init_vy: i32, y1: i32, y2: i32) -> i32 {
    let mut vy = init_vy;
    let mut y = 0;
    let mut maxy = 0;
    while y1 <= y {
        vy -= 1;
        y += vy;
        maxy = maxy.max(y);
        if y1 <= y && y <= y2 {
            return maxy;
        }
    }
    0
}


fn main() {
    let content = read_to_string("input").unwrap();

    let coorddefs: Vec<_> = content.trim().split(": ").last().unwrap().split(", ").collect();
    let y: Vec<_> = coorddefs[1].split('=').last().unwrap().split("..")
        .map(|s| s.parse::<i32>().unwrap()).collect();

    let result = (0..=500)
        .map(|vy| get_max_y(vy, y[0], y[1]))
        .filter(|&y| y > 0)
        .max()
        .unwrap();
    println!("result = {result:?}");
}
