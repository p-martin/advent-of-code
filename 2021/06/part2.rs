use std::fs::read_to_string;
use std::collections::HashMap;


fn main() {
    let mut timers = HashMap::new();
    for s in read_to_string("input").unwrap().trim().split(',') {
        *timers.entry(s.parse::<u64>().unwrap()).or_insert(0) += 1;
    }

    for _ in 1..=256 {
        let mut newtimers = HashMap::new();
        for (&t, &n) in timers.iter() {
            if t == 0 {
                *newtimers.entry(6u64).or_insert(0) += n;
                *newtimers.entry(8u64).or_insert(0) += n;
            } else {
                *newtimers.entry(t - 1).or_insert(0) += n;
            }
        }
        timers = newtimers;
    }

    let result: u64 = timers.values().sum();
    println!("result = {result:?}");
}
