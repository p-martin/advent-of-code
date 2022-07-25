use std::fs::read_to_string;


#[derive(Copy, Clone)]
enum Part {
    Open,
    Close,
    Comma,
    Num(u32),
}


fn parse_equation(s: &str) -> Vec<Part> {
    s.chars().map(|c| match c {
        '[' => Part::Open,
        ']' => Part::Close,
        ',' => Part::Comma,
        _ => Part::Num(c.to_digit(10).unwrap()),
    }).collect()
}


fn add_equations(a: &Vec<Part>, b: &Vec<Part>) -> Vec<Part> {
    let mut result = vec![Part::Open];
    for &elem in a.iter().chain([Part::Comma].iter()).chain(b.iter()) {
        result.append(&mut vec![elem]);
    }
    result.append(&mut vec![Part::Close]);
    result
}


fn explode_one(a: &mut Vec<Part>) -> bool {
    let mut depth = 0;
    let mut i = 0;
    for (j, &p) in a.iter().enumerate() {
        match p {
            Part::Open => {
                depth += 1;
                if depth >= 5 {
                    i = j;
                    break;
                }
            },
            Part::Close => {
                depth -= 1;
            },
            _ => {},
        }
    }
    if i > 0 {
        for j in 1..=i {
            if let Part::Num(val) = a[i - j] {
                if let Part::Num(expl) = a[i + 1] {
                    a[i - j] = Part::Num(val + expl);
                    break;
                }
            }
        }
        for j in i+5..a.len() {
            if let Part::Num(val) = a[j] {
                if let Part::Num(expl) = a[i + 3] {
                    a[j] = Part::Num(val + expl);
                    break;
                }
            }
        }
        for _ in 0..5 {
            a.remove(i);
        }
        a.insert(i, Part::Num(0));
    }
    i > 0
}


fn split_one(a: &mut Vec<Part>) -> bool {
    let mut i = 0;
    for (j, &p) in a.iter().enumerate() {
        if let Part::Num(val) = p {
            if val >= 10 {
                i = j;
                break;
            }
        }
    }
    if i > 0 {
        if let Part::Num(val) = a[i] {
            let lnum = val / 2;
            let rnum = val - lnum;
            a.remove(i);
            a.insert(i, Part::Close);
            a.insert(i, Part::Num(rnum));
            a.insert(i, Part::Comma);
            a.insert(i, Part::Num(lnum));
            a.insert(i, Part::Open);
        }
    }
    i > 0
}


fn calc_magnitude(a: &[Part]) -> u32 {
    if let [Part::Num(val)] = a {
        return *val;
    }
    let mut depth = 0;
    let i1 = 1;
    let mut i2 = 0;
    let mut i3 = 0;
    let mut i4 = 0;
    for (i, &p) in a.iter().enumerate() {
        match p {
            Part::Open => depth += 1,
            Part::Close => {
                depth -= 1;
                if depth == 0 {
                    if i3 != 0 {
                        i4 = i - 1;
                        break;
                    } else {
                        i2 = i - 1;
                    }
                }
            },
            Part::Comma if depth == 1 => {
                i2 = i - 1;
                i3 = i + 1;
            },
            _ => {},
        }
    }
    3 * calc_magnitude(&a[i1..=i2]) + 2 * calc_magnitude(&a[i3..=i4])
}


fn main() {
    let content = read_to_string("input").unwrap();
    let eqns: Vec<_> = content.trim().split('\n').map(|s| parse_equation(s)).collect();

    let mut total = eqns.first().unwrap().clone();
    for eqn in eqns.iter().skip(1) {
        total = add_equations(&total, eqn);
        let mut ch = true;
        while ch {
            ch = explode_one(&mut total);
            if !ch {
                ch = split_one(&mut total);
            }
        }
    }

    let result = calc_magnitude(&total[..]);
    println!("result = {result:?}");
}
