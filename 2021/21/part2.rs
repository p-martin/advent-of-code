use std::io::{BufReader, BufRead};
use std::fs::File;
use std::collections::HashMap;


fn get_num_wins(sc1: i32, sc2: i32, p1: i32, p2: i32,
                cache: &mut HashMap<(i32, i32, i32, i32), (u64, u64)>) -> (u64, u64)
{
    if cache.contains_key(&(sc1, sc2, p1, p2)) {
        return *cache.get(&(sc1, sc2, p1, p2)).unwrap();
    }
    if sc2 >= 21 {
        cache.insert((sc1, sc2, p1, p2), (0, 1));
        return (0, 1);
    }
    let mut w1 = 0;
    let mut w2 = 0;
    for d1 in [1, 2, 3] {
        for d2 in [1, 2, 3] {
            for d3 in [1, 2, 3] {
                let newp1 = (p1 - 1 + d1 + d2 + d3) % 10 + 1;
                let newsc1 = sc1 + newp1;
                let (nw2, nw1) = get_num_wins(sc2, newsc1, p2, newp1, cache);
                w1 += nw1;
                w2 += nw2;
            }
        }
    }
    cache.insert((sc1, sc2, p1, p2), (w1, w2));
    (w1, w2)
}


fn main() {
    let lines: Vec<_> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .collect();
    let p1: i32 = lines[0].split(": ").last().unwrap().parse().unwrap();
    let p2: i32 = lines[1].split(": ").last().unwrap().parse().unwrap();

    let mut cache = HashMap::new();
    let (sc1, sc2) = get_num_wins(0, 0, p1, p2, &mut cache);

    let result = sc1.max(sc2);
    println!("result = {result:?}");
}
