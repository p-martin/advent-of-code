use std::io::{BufReader, BufRead};
use std::fs::File;
use std::collections::{HashMap, BTreeMap};
use std::ops::AddAssign;


#[derive(Debug, Eq, PartialEq, Hash, Copy, Clone, Ord, PartialOrd)]
struct Point {
    x: i32,
    y: i32,
}


fn is_final_state(state: &BTreeMap<Point, char>, maxy: i32) -> bool {
    for y in 2..=maxy {
        for (x, c) in (3..10).step_by(2).zip("ABCD".chars()) {
            let p = Point{x: x as i32, y: y as i32};
            if !state.contains_key(&p) || state.get(&p).unwrap() != &c {
                return false;
            }
        }
    }
    true
}


fn serialize_state(state: &BTreeMap<Point, char>) -> String {
    let mut res = String::new();
    for p in state.keys() {
        let Point{x, y} = p;
        res.add_assign(x.to_string().as_str());
        res.push(',');
        res.add_assign(y.to_string().as_str());
        res.push(':');
        res.push(*state.get(&p).unwrap());
        res.push('\n');
    }
    res
}


fn move_amphipod(state: &BTreeMap<Point, char>, pt_txy: &Point, pt_xy: &Point, c: char,
                 mincost: i32, states: &mut HashMap<i32, Vec<BTreeMap<Point, char>>>,
                 mincost_for_state: &mut HashMap<String, i32>) {
    let costs = HashMap::from([('A', 1), ('B', 10), ('C', 100), ('D', 1000)]);
    let mut newstate = BTreeMap::new();
    for (&k, &v) in state.iter() {
        if &k != pt_xy {
            newstate.entry(k.clone()).or_insert(v);
        }
    }
    newstate.entry(pt_txy.clone()).or_insert(c);
    let newcost = mincost + ((pt_txy.y - pt_xy.y).abs() + (pt_txy.x - pt_xy.x).abs()) * costs
        .get(&c).unwrap();
    let key = serialize_state(&newstate);
    if !mincost_for_state.contains_key(&key) || mincost_for_state.get(&key).unwrap() > &newcost {
        states.entry(newcost).or_insert(vec![]).push(newstate);
        mincost_for_state.insert(key, newcost);
    }
}


fn solve(init_state: &BTreeMap<Point, char>) -> i32 {
    let maxy = init_state.iter().map(|p| p.0.y).max().unwrap();
    let mut mincost = 0;
    let mut states: HashMap<i32, Vec<BTreeMap<Point, char>>> = HashMap::new();
    states.insert(mincost, vec![init_state.clone()]);
    let mut mincost_for_state: HashMap<String, i32> = HashMap::new();
    mincost_for_state.entry(serialize_state(init_state)).or_insert(0);

    while states.len() > 0 {
        while !states.contains_key(&mincost) {
            mincost += 1;
        }
        let minstates = states.get_mut(&mincost).unwrap();
        let state = minstates.pop().unwrap();
        if is_final_state(&state, maxy) {
            return mincost;
        }
        if minstates.len() == 0 {
            states.remove(&mincost);
        }
        for (p, c) in state.iter() {
            let &Point{x, y} = p;
            if y >= 2 {  // from room to hallway
                if y > 2 && state.contains_key(&Point{x, y: y-1}) {
                    continue;  // blocked
                }
                if (y..=maxy).all(|yy| state.get(&Point{x, y: yy}).unwrap() == &"ABCD"
                        .chars().nth(((x-3)/2) as usize).unwrap()) {
                    continue;  // final place reached
                }
                let ty = 1;
                for tx in (1..=x-1).rev() {
                    if !vec![3, 5, 7, 9].contains(&tx) {
                        if state.contains_key(&Point{x: tx, y: ty}) {
                            break;  // hallway blocked
                        }
                        move_amphipod(&state, &Point{x: tx, y: ty}, &Point{x, y},
                                      *c, mincost, &mut states, &mut mincost_for_state);
                    }
                }
                for tx in x+1..12 {
                    if !vec![3, 5, 7, 9].contains(&tx) {
                        if state.contains_key(&Point{x: tx, y: ty}) {
                            break;  // hallway blocked
                        }
                        move_amphipod(&state, &Point{x: tx, y: ty}, &Point{x, y},
                                      *c, mincost, &mut states, &mut mincost_for_state);
                    }
                }
            } else {  // from hallway to target room
                let tx = match c {
                    'A' => 3,
                    'B' => 5,
                    'C' => 7,
                    'D' => 9,
                    _ => panic!("invalid char {:?}", c),
                };
                let mut ok = true;
                if tx < x {
                    for xx in (tx..=x-1).rev() {
                        if state.contains_key(&Point{x: xx, y: 1}) {
                            ok = false;  // blocked
                            break;
                        }
                    }
                } else {
                    for xx in x+1..tx+1 {
                        if state.contains_key(&Point{x: xx, y: 1}) {
                            ok = false;  // blocked
                            break;
                        }
                    }
                }
                if ok {
                    let mut ty = maxy;
                    while state.contains_key(&Point{x: tx, y: ty}) {
                        if state.get(&Point{x: tx, y: ty}).unwrap() != c {
                            ok = false;  // target room not yet cleared
                            break;
                        }
                        ty -= 1;
                    }
                    if ok {
                        move_amphipod(&state, &Point{x: tx, y: ty}, &Point{x, y},
                                      *c, mincost, &mut states, &mut mincost_for_state);
                    }
                }
            }
        }
    }
    panic!("no solution found");
}


fn main() {
    let lines: Vec<_> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .collect();

    let mut state = BTreeMap::new();
    for (y, line) in lines.iter().take(3).chain(["  #D#C#B#A#".to_string(),
        "  #D#B#A#C#".to_string()].iter()).chain(lines.iter().skip(3)).enumerate() {
        for (x, c) in line.chars().enumerate() {
            if "ABCD".contains(c) {
                state.insert(Point{x: x as i32, y: y as i32}, c);
            }
        }
    }

    let result = solve(&state);
    println!("result = {result:?}");
}
