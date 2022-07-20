use std::io::{BufReader, BufRead};
use std::fs::File;
use std::collections::HashMap;


fn count_paths(cave: &String, path: &Vec<&String>, graph: &HashMap<String, Vec<String>>,
               end: &String, twice: bool) -> usize {
    let mut result = 0;
    for nextcave in graph.get(cave).unwrap() {
        if nextcave == end {
            result += 1;
        } else {
            let twice_needed = nextcave.chars().all(|c| c.is_lowercase()) && path.contains(&nextcave);
            if !twice_needed || !twice {
                let mut newpath = path.clone();
                newpath.push(nextcave);
                result += count_paths(nextcave, &newpath, graph, end, twice_needed || twice);
            }
        }
    }
    result
}


fn main() {
    let lines: Vec<_> = BufReader::new(File::open("input").unwrap())
        .lines()
        .flatten()
        .collect();

    let mut graph: HashMap<String, Vec<String>> = HashMap::new();
    for line in lines.iter() {
        let parts: Vec<_> = line.split('-').collect();
        if let [a, b] = parts[..] {
            if a != "end" && b != "start" {
                graph.entry(a.to_string())
                    .and_modify(|v: &mut Vec<String>| { v.push(b.to_string()); })
                    .or_insert(vec![b.to_string()]);
            }
            if b != "end" && a != "start" {
                graph.entry(b.to_string())
                    .and_modify(|v: &mut Vec<String>| { v.push(a.to_string()); })
                    .or_insert(vec![a.to_string()]);
            }
        }
    }
    let start = "start".to_string();
    let end = "end".to_string();

    let result = count_paths(&start, &vec![&start], &graph, &end, false);
    println!("result = {result:?}");
}
