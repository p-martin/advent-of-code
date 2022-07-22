use std::fs::read_to_string;


fn hits_xy(init_vx: i32, init_vy: i32, x1: i32, x2: i32, y1: i32, y2: i32) -> bool {
    let mut vx = init_vx;
    let mut vy = init_vy;
    let mut x = 0;
    let mut y = 0;
    while x <= x2 && y1 <= y {
        vx = 0.max(vx - 1);
        vy -= 1;
        x += vx;
        y += vy;
        if x1 <= x && x <= x2 && y1 <= y && y <= y2 {
            return true;
        }
    }
    false
}


fn main() {
    let content = read_to_string("input").unwrap();

    let coorddefs: Vec<_> = content.trim().split(": ").last().unwrap().split(", ").collect();
    let x: Vec<_> = coorddefs[0].split('=').last().unwrap().split("..")
        .map(|s| s.parse::<i32>().unwrap()).collect();
    let y: Vec<_> = coorddefs[1].split('=').last().unwrap().split("..")
        .map(|s| s.parse::<i32>().unwrap()).collect();

    let mut result = 0;
    for vy in y[0]-1..=500 {
        for vx in 1..=x[1]+1 {
            if hits_xy(vx, vy, x[0], x[1], y[0], y[1]) {
                result += 1;
            }
        }
    }
    println!("result = {result:?}");
}
