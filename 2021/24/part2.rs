use std::fs::read_to_string;


fn calc_forward(z: i32, d: i32, a: i32, b: i32, c: i32) -> i32 {
    let x = ((z % 26 + b) != d) as i32;
    (z / a) * (25*x + 1) + (d + c)*x
}


fn calc_backward(z_target: i32, d: i32, coeffs: (i32, i32, i32)) -> Option<i32> {
    let (a, b, c) = coeffs;
    let x = (a != 26) as i32;
    let mut z = (z_target - (d + c)*x) / (25*x + 1);
    if x == 0 {
        z = a*z + d - b;
    }
    if calc_forward(z, d, a, b, c) == z_target {
        return Some(z);
    }
    None
}


fn solve(coeff_list: &Vec<(i32, i32, i32)>, pos: usize, z_target: i32) -> String {
    for d in 1..=9 {
        if let Some(new_z_target) = calc_backward(z_target, d, coeff_list[pos]) {
            if pos == 0 {
                return d.to_string();
            }
            let next_d = solve(coeff_list, pos - 1, new_z_target);
            if !next_d.is_empty() {
                return next_d + d.to_string().as_str();
            }
        }
    }
    "".to_string()
}


fn main() {
    let content = read_to_string("input").unwrap();

    let mut coeff_list = vec![];
    for dblock in content.trim().split("inp w\n").skip(1) {
        let lines: Vec<_> = dblock.split('\n').collect();
        let a = lines[3].split(' ').last().unwrap().parse::<i32>().unwrap();
        let b = lines[4].split(' ').last().unwrap().parse::<i32>().unwrap();
        let c = lines[14].split(' ').last().unwrap().parse::<i32>().unwrap();
        coeff_list.push((a, b, c));
    }

    let result = solve(&coeff_list, coeff_list.len() - 1, 0);
    println!("result = {result:?}");
}
